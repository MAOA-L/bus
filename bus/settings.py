"""
Django settings for bus project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'adscqp^bynz(gkz)8-#8b+66+6o1&ym147#dpfor0wmvu2x5_&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 跨域
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*'
)
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'unit',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'utils.exception_handler.CustomExceptionHandler',

    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # LimitOffsetPagination 分页风格
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',  # LimitOffsetPagination 分页风格
    'PAGE_SIZE': 10,  # 每页显示多少个
}
ROOT_URLCONF = 'bus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'bus.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

DATETIME_FORMAT_COMMON = "%Y-%m-%d %H:%M:%S"
DATETIME_NOS_FORMAT = "%Y-%m-%d %H:%M"
DATE_FORMAT_COMMON = "%Y-%m-%d"
DATE_FORMAT_COMMON_CN = "%Y年%m月%d日"
TIME_FORMAT_COMMON = "%H:%M"
TIME_FORMAT_12H_MODE = "%I:%M"
TIME_FORMAT_12H_MODE_WITH_SUFFIX = "%I:%M(%p)"
TIME_FORMAT_TIME_COMMON = "%H:%M:%S"

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static").replace('\\', '/')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

FILES_URL = '/files/'
FILES_ROOT = os.path.join(BASE_DIR, 'files').replace('\\', '/')

django_profiles_active = 'dev'  # dev 本地开发  test  测试   prod 生产
if django_profiles_active == 'dev':
    from bus.settings_dev import *
elif django_profiles_active == 'prod':  # 线上
    from bus.settings_prod import *
