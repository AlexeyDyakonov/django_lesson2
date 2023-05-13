import os

from environs import Env

env = Env()
env.read_env()

HOST = env.str('HOST')
PORT = env.str('PORT')
NAME = env.str('NAME')
USER = env.str('USER')
PASSWORD = env.str('PASSWORD')
SECRET_KEY_BD = env.str('SECRET_KEY')
LANGUAGE_CODE_BD = env.str('LANGUAGE_CODE')
TIME_ZONE_BD = env.str('TIME_ZONE')
debug = env.bool('DEBUG', False)
allowed_hosts = env.list("ALLOWED_HOSTS", ["localhost:8000"])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': HOST,
        'PORT': PORT,
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = SECRET_KEY_BD

DEBUG = debug

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = allowed_hosts


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = LANGUAGE_CODE_BD

TIME_ZONE = TIME_ZONE_BD

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
