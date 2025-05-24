
SECRET_KEY = '123'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'WebCraftLauncher',
]

ROOT_URLCONF = 'WebCraftLauncher.urls'
ASGI_APPLICATION = 'WebCraftLauncher.asgi.application'

STATIC_URL = '/static/'

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]
