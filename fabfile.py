from fabric import Connection
from invoke import task
import subprocess
import sys

DEV = dict()
PROD = dict()

USER = 'thunderatz'
HOST = 'thunderatz.org'

PROJECT = 'ThunderSite'

DEV['app'] = 'thundersitev2_dev'
DEV['app_root'] = '/home/{}/webapps/{}'.format(USER, DEV['app'])
DEV['app_port'] = 25553
DEV['static_root'] = '/home/{}/webapps/tsite_dev_static'.format(USER)
DEV['gunicorn_workers'] = 1
DEV['gunicorn_pidfile'] = '{}/gunicorn.pid'.format(DEV['app_root'])
DEV['gunicorn_logfile'] = '/home/{}/logs/user/gunicorn_dev.log'.format(USER)
DEV['venv_dir'] = '{}/tsitedev_venv'.format(DEV['app_root'])

PROD['app'] = 'thundersitev2_prod'
PROD['app_root'] = '/home/{}/webapps/{}'.format(USER, PROD['app'])
PROD['app_port'] = 23449
PROD['static_root'] = '/home/{}/webapps/thundersitev2_static'.format(USER)
PROD['gunicorn_workers'] = 2
PROD['gunicorn_pidfile'] = '{}/gunicorn.pid'.format(PROD['app_root'])
PROD['gunicorn_logfile'] = '/home/{}/logs/user/gunicorn_dev.log'.format(USER)
PROD['venv_dir'] = '{}/tsiteprod_venv'.format(PROD['app_root'])

PYTHON_BIN = 'python'

def start_server(conn, env):
    print('Starting server...')
    with conn.cd(env['app_root'] + '/' + PROJECT):
        conn.run(_gunicorn(env))

def stop_server(conn, env):
    print('Stopping server...')
    if not conn.run('cat {}'.format(env['gunicorn_pidfile'])).ok:
        return

    conn.run('kill $(cat {})'.format(env['gunicorn_pidfile']))
    # conn.run('rm {}'.format(env['gunicorn_pidfile']))

def install_dependencies(conn, env):
    print('Installing dependencies...')
    with conn.cd(env['app_root'] + '/' + PROJECT):
        conn.run('source {}/bin/activate && pip install -r requirements.txt'.format(
            env['venv_dir']
        ))

def update_db(conn, env):
    print('Updating databases...')
    with conn.cd(env['app_root'] + '/' + PROJECT):
        conn.run('source {}/bin/activate && python manage.py migrate --noinput'.format(
            env['venv_dir']
        ))

def collect_static(conn, env):
    print('Collecting staticfiles...')
    with conn.cd(env['app_root'] + '/' + PROJECT):
        conn.run('source {}/bin/activate && python manage.py collectstatic -v0 --noinput --clear'.format(
            env['venv_dir']
        ))

def push_dev(conn, env):
    print('Pushing changes to develop branch...')
    r = subprocess.run(['git', 'checkout', 'develop'])
    if r.returncode != 0:
        print('Error on git checkout develop')
        return

    r = subprocess.run(['git', 'add', '-A'])
    if r.returncode != 0:
        print('Error on git add')
        return

    commit = input("Commit message: ")
    r = subprocess.run(['git', 'commit', '-m', commit])
    if r.returncode != 0:
        print('Error on git commit')
        return

    r = subprocess.run(['git', 'push', 'origin', 'develop'])
    if r.returncode != 0:
        print('Error on git push')
        return

    with conn.cd(env['app_root'] + '/' + PROJECT):
        conn.run('git pull origin develop')

def push_prod(conn, env):
    print('Getting changes from master branch...')

    with conn.cd(env['app_root'] + '/' + PROJECT):
        conn.run('git pull origin master')

def _gunicorn(env):
    return '{}/bin/gunicorn --log-file {} -b 127.0.0.1:{} -D -w {} --pid {} thundersite.wsgi'.format(
        env['venv_dir'],
        env['gunicorn_logfile'],
        env['app_port'],
        env['gunicorn_workers'],
        env['gunicorn_pidfile']
    )

@task
def deploy_dev(conn):
    stop_server(conn, DEV)
    push_dev(conn, DEV)
    install_dependencies(conn, DEV)
    update_db(conn, DEV)
    collect_static(conn, DEV)
    start_server(conn, DEV)

    with conn.cd(DEV['static_root'] + '/CACHE/css'):
        conn.run('postcss *.css --replace --use autoprefixer')

@task
def deploy_prod(conn):
    stop_server(conn, PROD)
    push_prod(conn, PROD)
    install_dependencies(conn, PROD)
    update_db(conn, PROD)
    collect_static(conn, PROD)
    start_server(conn, PROD)

    with conn.cd(PROD['static_root'] + '/CACHE/css'):
        conn.run('postcss *.css --replace --use autoprefixer')


@task
def start_dev_server(conn):
    start_server(conn, DEV)

@task
def start_prod_server(conn):
    start_server(conn, PROD)
