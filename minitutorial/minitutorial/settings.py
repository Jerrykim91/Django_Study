"""
Django settings for minitutorial project.

Generated by 'django-admin startproject' using Django 2.2.5.

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
SECRET_KEY = 'u50j&5arg=p5dgelegpc1_m5l$=!z)p5#9ug6=9(qwpt2e5@7p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'board',                       # 등록할 app name
    'django.contrib.admin',        # django admin app
    'django.contrib.auth',         # django auth app
    'django.contrib.contenttypes', # 다양한 종류의 모델데이터를 관리할 수 있게 도와주는 app.
    'django.contrib.sessions',     # client info를 세션에서 관리하도록 하는 framework
    'django.contrib.messages',     # 컨트롤러에서 발생한 info를 view에서 쉽게 접근하도록 연결하는 framework
    'django.contrib.staticfiles',  # html, css, js 파일등의 정적파일 들을 관리해주는 framework
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'minitutorial.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'minitutorial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        # sqlite DB사용시
            #'ENGINE': 'django.db.backends.sqlite3',
            #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

            #  mysql
            # 'ENGINE': 'django.db.backends.mysql',
            # 'NAME': 'DB명',
            # 'USER': '아이디명',
            # 'PASSWORD' : '암호',
            # 'HOST' : '127.0.0.1',
            # 'PORT' : '포토번호'

            # oracle(admin)
            'ENGINE': 'django.db.backends.oracle',
            'NAME': 'xe', #SID
            'USER': 'admin',
            'PASSWORD' : '1234',
            'HOST' : '192.168.99.100',
            'PORT' : '32764'

            # 'ENGINE': 'django.db.backends.oracle',
            # 'NAME': 'xe', #SID
            # 'USER': 'minitutorial',
            # 'PASSWORD' : '1234',
            # 'HOST' : '192.168.99.100',
            # 'PORT' : '32764'

            # GDP_PROJECT
            # 'ENGINE': 'django.db.backends.oracle',
            # 'NAME': 'xe',
            # 'USER' : 'GDP_PROJECT',
            # 'PASSWORD' : '1234',
            # 'HOST' : '192.168.99.100',
            # 'PORT' : '32764'

            # 'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul' # 시간대를 서울로 변경
# TIME_ZONE = 'UTC'


USE_I18N = True

USE_L10N = True

USE_TZ = False # 기본 시간대(UTC)를 사용하지 않겠다고 변경
# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
