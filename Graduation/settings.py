"""
Django settings for Graduation project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@9u&x%21g7ut8l9#ij!h*qw6d5s(%6e&!y-p+%*d5&p92y-9g&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.3.110', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.sitemaps',

    'personage.apps.PersonageConfig',
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

ROOT_URLCONF = 'Graduation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
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

WSGI_APPLICATION = 'Graduation.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Graduation',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '3306',
    }
}

# 缓存配置
CACHES = {
    # django存缓默认位置,redis 0号库
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # django session存 reidis 1 号库（现在基本不需要使用）
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 图形验证码，存redis 2号库
    "img_code": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient",
                    }
    }
}
# 配置session使用redis存储
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 配置session存储的位置: 使用cache中的 session配置
SESSION_CACHE_ALIAS = "session"

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# python manage.py collectstatic
# 可以把静态文件收集到（复制到） STATIC_ROOT目录
STATIC_ROOT = BASE_DIR / 'static'

# 共用的静态文件
STATICFILES_DIRS = (
    BASE_DIR / "common_static",
)

#  存放用户上传的文件
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 使用新admin
# 注册用户开放
USERS_REGISTRATION_OPEN = True
# 用户验证电子邮件
USERS_VERIFY_EMAIL = True
# 用户在激活时自动登录
USERS_AUTO_LOGIN_ON_ACTIVATION = True
# 用户通过电子邮件确认超时日期
USERS_EMAIL_CONFIRMATION_TIMEOUT_DAYS = 3
# 指定密码的最小长度:
USERS_PASSWORD_MIN_LENGTH = 5
# 指定密码的最大长度:
USERS_PASSWORD_MAX_LENGTH = None
# 复杂性验证器，检查密码强度
USERS_CHECK_PASSWORD_COMPLEXITY = True
# 用户的垃圾邮件保护
USERS_SPAM_PROTECTION = False

# 网站邮箱
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'tangzheng972631576@163.com'
EMAIL_HOST_PASSWORD = 'VVWQEBJRWGUVIUPB'
DEFAULT_FROM_EMAIL = 'tangzheng <tangzheng972631576@163.com>'

# 用户密码策略
USERS_PASSWORD_POLICY = 0
# 用户电子邮件域黑名单
USERS_EMAIL_DOMAINS_BLACKLIST = []
# 用户电子邮件域白名单
USERS_EMAIL_DOMAINS_WHITELIST = []
# 用户创建超级用户
USERS_CREATE_SUPERUSER = True
