# coding=utf-8
import os

# Django settings for BriefWeb project.
DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),
                               os.pardir))
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'brief.db',  # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',  # Set to empty string for default.
    }
}

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'blog',
    'albums',
    'translation',
    'resource',
    'brief',
    'documents',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = "zh-Hans"

USE_I18N = True

USE_L10N = True

USE_TZ = False

SITE_ID = 1

DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'

# MEDIA_ROOT = ''

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static", "dist"),
]

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")

DOCS_URL = "/docs/"

DOCS_ROOT = os.path.join(PROJECT_ROOT, "docs", "_build", "html")


SECRET_KEY = ')^-shkpf*knu5mo=t%7!madeling#a!6ei4a8dv%qjq!*(&=^ar2a'


ROOT_URLCONF = 'BriefWeb.urls'

WSGI_APPLICATION = 'BriefWeb.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# 修改上传时文件在内存中可以存放的最大size为10m
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760

try:
    from .server_conf import *
except ImportError:
    pass

# try:
#     from .local_conf import *
# except ImportError:
#     pass
