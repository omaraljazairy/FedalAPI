"""
Django settings for api project.
Generated by 'django-admin startproject' using Django 2.0.5.
For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
# coverage run --source=tests manage.py test
# --exclude-tag=skip2 --setting=tests.test_settings  tests/spanglish -v 2

import os
import datetime
# from tests import test_env

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@j(te*j8xl8ewa2n(vt*x-2$fz5@&z!orwbq=mx@f%l2(nze#i'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
IS_TESTING = True
ALLOWED_HOSTS = []
FIXTURE_DIRS = 'fixtures/'

AWS_LOGGER_NAME = "unitest"
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_nose',
    'spanglish',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(process)d:%(name)s]\
             [%(funcName)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/test.log'),
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'spanglish': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'wipecardetailing': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'email': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


ROOT_URLCONF = 'api.urls'


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


WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('ENGINE', 'django.db.backends.mysql'),
        'NAME': os.environ.get('DB_DATABASE', 'Fedal'),
        'USER': os.environ.get('DB_USER', 'admin'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '3306'),
    },
    # 'spanglish': {
    #     'ENGINE': test_env.DB['ENGINE'],
    #     'NAME': test_env.DB['NAME'],
    #     'USER': test_env.DB['USER'],
    #     'PASSWORD': test_env.DB['PASSWORD'],
    #     'HOST': test_env.DB['HOST'],
    #     'PORT': test_env.DB['PORT']
    # },
    # 'wipecardetailing': {
    #     'ENGINE': test_env.DB['ENGINE'],
    #     'NAME': test_env.DB['NAME'],
    #     'USER': test_env.DB['USER'],
    #     'PASSWORD': test_env.DB['PASSWORD'],
    #     'HOST': test_env.DB['HOST'],
    #     'PORT': test_env.DB['PORT']
    # }
}

DATABASE_RAW_TABLES = {
    "category": "Category ",
    "language": "Language",
    "sentence": "Sentence",
    "translation": "Translation",
    "verb": "Verb",
    "word": "Word",
}
#
# DATABASE_ROUTERS = [
#     'spanglish.dbrouter.DBRouter',
#     'wipecardetailing.dbrouter.DBRouter',
# ]

# cache server

# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': test_env.REDIS_LOCATION,
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "PASSWORD": test_env.REDIS_PASSWORD
#             },
#     }
# }

# CACHE_TTL = 1


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


# CUSTOM_USER_MODEL = 'spanglish.Profile'


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

REST_FRAMEWORK = {
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S%z',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10000/day',
        'user': '10000/day',
        'spanglish': '10000/min',
        'wipecardetailing': '10000/min',
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=1420),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': datetime.timedelta(minutes=1420),
    'SLIDING_TOKEN_REFRESH_LIFETIME': datetime.timedelta(days=1),
}

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_TO = 'test@fedal.nl'

API_KEY_CUSTOM_HEADER = "HTTP_X_API_KEY"

CORS_ORIGIN_ALLOW_ALL =  True

# Nose unitests setting
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--cover-erase',
    '--with-coverage',
    '--cover-package=spanglish',
    '--with-xunit',
    '--cover-html',
    '--cover-html-dir=tests/htmlcov',
    '--cover-xml',
    '--cover-xml-file=unittests.xml',
    "--ignore-files='^admin.py', '^\\.', '^_', '^setup\\.py$'",
    '--verbosity=2'
]

FIXTURES = {
    'spanglish': os.path.join(BASE_DIR,
                              'spanglish/tests/fixtures/spanglish.json'),
}

# setup.py sdist --format=zip egg_info --tag-date --tag-build=alpha
# nose.config: INFO: Ignoring files matching ['^\\.', '^_', '^setup\\.py$']
# admin - myadmin_2020
# omar - iamomar_2020
# auth http GET :8000/api/sampleapi "Authorization: Token 5c835fce979905a
# test command : ../bin/python3.6 manage.py test --settings=tests.settings -s campaigns
# load fixtures: python3.6 manage.py loaddata --database=Q_read campaigns/tests/fixtures/campaigns.yaml
# dump campaigns python3.6 manage.py dumpdata spanglish --database=spanglish --indent 4 --format=json
# dump enum: python3.6 manage.py dumpdata campaigns.ServiceModel campaigns.ServiceType campaigns.ShortCode campaigns.Gateway campaigns.DomainBrand campaigns.Country campaigns.Company --database=Enum_read --indent 4 > campaigns/tests/fixtures/enum.json
# dump core: python3.6 manage.py dumpdata campaigns.ServiceOverride campaigns.ServiceMetadata campaigns.Service --database=CORE_read --indent 4 > campaigns/tests/fixtures/core.json
# dump q: python3.6 manage.py dumpdata campaigns.adsSession campaigns.adsSessionMetadata campaigns.adsSessionHistory campaigns.Adsad campaigns.Adsparameters campaigns.Madspartner campaigns.Madszone campaigns.Backend --database=Q_read --indent 4 > campaigns/tests/fixtures/q.json
# run test ../bin/python3.6 manage.py test --settings=tests.settings -s campaigns services/tests/
# inspect_db ../bin/python manage.py inspectdb --database=spanglish > spanglish/models.py
# wipecardetailing api-key: 7MMG9BDn.VArqTdzCNjtuRYORu0gm7V9TT9stvodj
# ====================================================================
