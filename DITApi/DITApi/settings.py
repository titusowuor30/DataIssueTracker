"""
Django settings for DITApi project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from .juzmin import JAZZMIN_SETTINGS
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5=@j@xy=c*ku8)^8+i@i#n1rq__c#n8y6p!p5q@v=8%7xu0c07'
EMAIL_APP_PASS=os.environ.get('EMAIL_APP_PASS','tvrmtjseseegiccc')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG",True)

ALLOWED_HOSTS = ['*']
X_FRAME_OPTIONS = 'SAMEORIGIN'


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    #myapps
    'DQIT_Endpoint',
    'DQITAuth',
    #third pirty
    'django_countries',
    'timezone_field',
    'user_agents',
    'tinymce',
    'widget_tweaks',
]

AUTH_USER_MODEL = 'DQITAuth.CustomUser'
SCHEDULER_API_ENABLED = True
SITE_ID=1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.contrib.sites.middleware.SiteMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'DQITAuth.middleware.TimezoneMiddleware',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '{message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',  # Adjust this level to control the log verbosity.
    },
    'loggers': {
        'ditapi_logger': {
            'handlers': ['console'],
            'level': 'DEBUG',  # Adjust this level to control the Django-specific log verbosity.
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',  # Adjust this level to control the Django-specific log verbosity.
            'propagate': False,
        },
    },
}


ROOT_URLCONF = 'DITApi.urls'

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

WSGI_APPLICATION = 'DITApi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.mysql', #'mysql.connector.django',
#         'NAME': 'dqits',
#         'USER': 'newuser',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',  # Usually 'localhost' or '127.0.0.1'
#         'PORT': '3306',  # Default MySQL port is 3306
#         # 'OPTIONS': {
#         #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         #     'charset': 'utf8mb4',
#         # },
#         # 'CONN_MAX_AGE': 600,
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get('DB_HOST','localhost'),
        'PORT': os.environ.get('DB_PORT','3306'),
        'NAME': os.environ.get('DB_NAME','dqits'),
        'USER': os.environ.get('DB_USER','dqitsuser'),
        'PASSWORD': os.environ.get('DB_PASSWORD','DQITs@123'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# AUTHENTICATION_BACKENDS = [
#     'DQITAuth.backends.PasswordPolicyBackend',  # Add your backend here
#     'django.contrib.auth.backends.ModelBackend',
# ]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:5173',
)

SPECTACULAR_SETTINGS = {
    'TITLE': 'DQITs API',
    'DESCRIPTION': 'DQITs API',
    'VERSION': '1.0.0',
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
MEDIA_URL = '/media/'  # This is just for url i.e https://l.me/media/l.jpg
# This is the folder the image will be uploaded
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_FILTER_INSPECTORS': [
        'rest_framework.filters.DjangoFilterInspector',
    ],
    'SEARCH_PARAM': 'q',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_csv.renderers.CSVRenderer',  # Add this line for CSV support
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

TINYMCE_DEFAULT_CONFIG = {
    'height': 400,
    'width': 800,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'plugins': 'advlist autolink lists link image charmap print preview anchor, searchreplace visualblocks code fullscreen, insertdatetime media table contextmenu paste code help wordcount',
    'toolbar': 'undo redo | formatselect | bold italic backcolor | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat | help',
    'menubar': 'file edit view insert format tools table help',
}
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
