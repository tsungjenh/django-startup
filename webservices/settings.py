"""
Django settings for django-http project.
"""
import os
from service.libs.jsonlogger import JsonFormatter
import pymysql

pymysql.install_as_MySQLdb()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'l0sehz=^#tkx06()3et&3jtxtatr(5l^x6el2)uhc*dp7pvw8i'

DEBUG = True

SESSION_KEY = "session_id"

ALLOWED_HOSTS = ['*']

COUNTRY = 'cn'

INSTALLED_APPS = [
    'django.contrib.sessions',
    'scripts',
    'api',
    'service.biz.user'
]

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'webservices.middleware.ApiMiddleware',
)

WEB_APP_ROOT_URL = ''

ROOT_URLCONF = 'webservices.urls'

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

WSGI_APPLICATION = 'webservices.wsgi.application'

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Chongqing'

# LOG CONFIG
LOG_DIR = "./log/"
LOG_FILE = os.path.join(LOG_DIR, "django_http.log")
LOG_ERR_FILE = os.path.join(LOG_DIR, "django_http.err.log")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json_stat': {
            '()': JsonFormatter,
            'format': '%(message)s'
        },
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'formatter': 'simple',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': LOG_FILE,
        },
        'err_file': {
            'level': 'WARN',
            'formatter': 'simple',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': LOG_ERR_FILE,
        },
    },
    'loggers': {
        'django_http': {
            'handlers': ['file' ],
            'level': 'INFO',
            'propagate': False
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'file', 'err_file', ] if DEBUG else ['file', 'err_file'],
        'propagate': True
    }
}

FS_DIR = './log/django_http/'


try:
    from webservices.env_settings import *
except ImportError:
    from webservices.settings_test import *
