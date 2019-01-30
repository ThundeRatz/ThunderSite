import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    "reset_migrations",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "social_django",
    "compressor",
    "ckeditor",
    "landing",
    "projects",
    "news",
    "members",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

ROOT_URLCONF = "thundersite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ]
        },
    }
]

WSGI_APPLICATION = "thundersite.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_L10N = True

USE_TZ = True

############## STATIC ##############
STATIC_URL = "/local_static/"

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

COMPRESS_PRECOMPILERS = (
    (
        "text/x-sass",
        "/home/thunderatz/bin/sassc {infile} {outfile}",
    ),
)

############## MEDIA ##############
MEDIA_URL = "/media/"

############### CKEDITOR ##############
CKEDITOR_UPLOAD_PATH = "ckeditor/"

CKEDITOR_CONFIGS = {"default": {"toolbar": "standard", "extraPlugins": "youtube"}}

AUTHENTICATION_BACKENDS = (
    "social_core.backends.open_id.OpenIdAuth",
    "social_core.backends.google.GoogleOpenId",
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

LOGIN_URL = "admin:login"
LOGIN_REDIRECT_URL = "admin:index"

SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = ["thunderatz.org"]
SOCIAL_AUTH_LOGIN_ERROR_URL = "/403/"

try:
    from .local_settings import *
except ImportError as e:
    print("local_settings.py not found, create it with these settings:")
    print("    ALLOWED_HOSTS")
    print("    MEDIA_ROOT")
    print("    STATIC_ROOT")
    print("    SECRET_KEY")
    print("    DEBUG")
    print("    COMPRESS_ENABLED")
    print("    DATABASES")
    print("    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
    print("    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")
