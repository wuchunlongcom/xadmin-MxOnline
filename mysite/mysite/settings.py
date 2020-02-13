# -*- coding: UTF-8 -*-
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm*#@l&s7f@ad&ei!d=bxx+@6b0hqoy-sql#4zo00s2%^s@8rbv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# 设置auth允许的函数
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)


# LANGUAGES = (
#     ('en', _('English')),
#     ('zh-hans', _('Chinese')),
# )

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'xadmin',
    # django-crispy-forms DRY 美化form表单
    'crispy_forms',
    # django-reversion 版本控制
    'reversion',
    
    #'app.apps.AppConfig',
    'import_export',
    
    'captcha',    
    'course.apps.CourseConfig',
    'operation.apps.OperationConfig',
    'organization.apps.OrganizationConfig',
    'users.apps.UsersConfig',     
    'DjangoUeditor',
    'pure_pagination',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #添加图片处理器，为了在课程列表中前面加上MEDIA_URL
                'django.template.context_processors.media',

            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'

LOCALE_PATHS = (
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "../locale"),
)

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
SITE_ROOT = os.path.dirname(os.path.abspath(__file__)) # ../mysite/mysite
SITE_ROOT = os.path.abspath(os.path.join(SITE_ROOT, '..')) # ../mysite


# 定义静态文件的目录 BASE_DIR: ../mysite
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static_common').replace('\\', r'/'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# 在导入数据时使用数据库事务，默认False
IMPORT_EXPORT_USE_TRANSACTIONS = True

# 定义图片存放的目录
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 翻译文件所在目录
LOCALE_PATHS = (
    os.path.join(os.path.dirname(BASE_DIR), 'xadmin', 'locale'),
)

AUTH_USER_MODEL = 'users.UserProfile'
# 配置邮箱发邮件的相关功能 
EMAIL_USE_TLS= True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #这一项是固定的
EMAIL_HOST = 'smtp.163.com' # SMTP服务器主机 163
EMAIL_PORT = 25 # smtp服务固定的端口是25
EMAIL_HOST_USER = 'wcl6005@163.com' #发送邮件的邮箱
EMAIL_HOST_PASSWORD = 'wcl6005' #在邮箱中设置的客户端授权密码
EMAIL_FROM = 'python<wcl6005@163.com>' #收件人看到的发件人 <此处要和发送邮件的邮箱相同>


# print(LOCALE_PATHS)

# 生成需要翻译的文件
# python manage.py makemessages -l zh_Hans
# 编译翻译
# python manage.py compilemessages -l zh_Hans
