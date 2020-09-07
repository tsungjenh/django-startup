DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_startup',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '192.168.1.5',
        'PORT': '3306'
    },
}

USER_REDIS_ADDR = "redis://@192.168.1.7:6379/0"

