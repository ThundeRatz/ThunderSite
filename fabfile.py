from fabric import Connection
from invoke import task
import subprocess
import sys

DEV = dict()
PROD = dict()

USER = "tr"
HOST = "thunderatz.org"

PROJECT = "ThunderSite"

DEV["app"] = "thundersite_dev"
DEV["app_root"] = f"/home/{USER}/apps/{DEV['app']}"
DEV["app_socket"] = f"unix:{DEV['app_root']}/{DEV['app']}.sock"
DEV["static_root"] = f"{DEV['app_root']}/static"
DEV["gunicorn_workers"] = 1
DEV["gunicorn_pidfile"] = f"{DEV['app_root']}/gunicorn.pid"
DEV["gunicorn_logfile"] = f"/home/{USER}/logs/gunicorn_dev.log"
DEV["venv_dir"] = f"{DEV['app_root']}/venv"

PROD["app"] = "thundersite"
PROD["app_root"] = f"/home/{USER}/apps/{PROD['app']}"
PROD["app_socket"] = f"unix:{PROD['app_root']}/{PROD['app']}.sock"
PROD["static_root"] = f"{PROD['app_root']}/static"
PROD["gunicorn_workers"] = 2
PROD["gunicorn_pidfile"] = f"{PROD['app_root']}/gunicorn.pid"
PROD["gunicorn_logfile"] = f"/home/{USER}/logs/gunicorn.log"
PROD["venv_dir"] = f"{PROD['app_root']}/venv"

PYTHON_BIN = "python"


def start_server(conn, env):
    print("Starting server...")
    with conn.cd(env["app_root"] + "/" + PROJECT):
        conn.run(_gunicorn(env))


def stop_server(conn, env):
    print("Stopping server...")
    if not conn.run("cat {}".format(env["gunicorn_pidfile"])).ok:
        return

    conn.run("kill (cat {})".format(env["gunicorn_pidfile"]))
    # conn.run('rm {}'.format(env['gunicorn_pidfile']))


def install_dependencies(conn, env):
    print("Installing dependencies...")
    with conn.cd(env["app_root"] + "/" + PROJECT):
        conn.run(
            "source {}/bin/activate.fish && pip install -r requirements.txt".format(
                env["venv_dir"]
            )
        )


def update_db(conn, env):
    print("Updating databases...")
    with conn.cd(env["app_root"] + "/" + PROJECT):
        conn.run(
            "source {}/bin/activate.fish && python manage.py migrate --noinput".format(
                env["venv_dir"]
            )
        )


def collect_static(conn, env):
    print("Collecting staticfiles...")
    with conn.cd(env["app_root"] + "/" + PROJECT):
        conn.run(
            "source {}/bin/activate.fish && python manage.py collectstatic -v0 --noinput --clear".format(
                env["venv_dir"]
            )
        )


def push_dev(conn, env):
    print("Pushing changes to develop branch...")
    r = subprocess.run(["git", "checkout", "develop"])
    if r.returncode != 0:
        print("Error on git checkout develop")

    r = subprocess.run(["git", "add", "-A"])
    if r.returncode != 0:
        print("Error on git add")

    commit = input("Commit message: ")
    r = subprocess.run(["git", "commit", "-m", commit])
    if r.returncode != 0:
        print("Error on git commit")

    r = subprocess.run(["git", "push", "origin", "develop"])
    if r.returncode != 0:
        print("Error on git push")

    with conn.cd(env["app_root"] + "/" + PROJECT):
        conn.run("git pull origin develop")


def push_prod(conn, env):
    print("Getting changes from master branch...")

    with conn.cd(env["app_root"] + "/" + PROJECT):
        conn.run("git pull origin master")


def _gunicorn(env):
    return "{}/bin/gunicorn --log-file {} -b {} -D -w {} --pid {} thundersite.wsgi".format(
        env["venv_dir"],
        env["gunicorn_logfile"],
        env["app_socket"],
        env["gunicorn_workers"],
        env["gunicorn_pidfile"],
    )


def cache_process_static(conn, env):
    conn.run("rm -r " + env["static_root"] + "/CACHE/css")

    with conn.cd(env["app_root"] + "/" + PROJECT):
        conn.run(
            "source {}/bin/activate.fish && python manage.py compress".format(
                env["venv_dir"]
            )
        )

    with conn.cd(env["static_root"] + "/CACHE/css"):
        conn.run("postcss *.css --replace --use autoprefixer")


@task
def deploy_dev(conn):
    stop_server(conn, DEV)
    push_dev(conn, DEV)
    install_dependencies(conn, DEV)
    update_db(conn, DEV)
    collect_static(conn, DEV)
    start_server(conn, DEV)


@task
def deploy_prod(conn):
    stop_server(conn, PROD)
    push_prod(conn, PROD)
    install_dependencies(conn, PROD)
    update_db(conn, PROD)
    collect_static(conn, PROD)
    cache_process_static(conn, PROD)
    start_server(conn, PROD)


@task
def start_dev_server(conn):
    start_server(conn, DEV)


@task
def stop_dev_server(conn):
    stop_server(conn, DEV)


@task
def start_prod_server(conn):
    start_server(conn, PROD)


@task
def restart_prod_server(conn):
    stop_server(conn, PROD)
    start_server(conn, PROD)
