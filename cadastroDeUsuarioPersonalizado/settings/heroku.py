import environ

from cadastroDeUsuarioPersonalizado.settings.base import *
# app stormy-harbor-54697.
env = environ.Env()

DEBUG = env.bool('DEBUG', False)

SECRET_KEY = env('SECRET_KEY')
#SECRET_KEY=1BV#@rd2G*@**3
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default': env.db(),
}