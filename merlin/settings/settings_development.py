from merlin.settings.base import *

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

from .database_info import *

DATABASES = {
    'default': {
        'ENGINE': ENGINE,
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': PORT,
    }
}
