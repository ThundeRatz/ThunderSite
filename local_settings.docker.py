import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ["0.0.0.0"]
MEDIA_ROOT = os.path.join(BASE_DIR, "wget/thunderatz.org/media/")
STATIC_ROOT = os.path.join(BASE_DIR, "wget/thunderatz.org/static/")

SECRET_KEY = "essa_eh_a_chave_secreta"

VENV_ROOT = "/usr/local"
DEBUG = True
COMPRESS_ENABLED = False

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "thundersite-database",
        "PORT": "5432",
    }
}
