"""
WSGI config for Shueisha project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
#Importa librería para acceder a las carpetas de la computadora
import os

#Import necesario para el correcto funcionamiento de la página web
from django.core.wsgi import get_wsgi_application

#Funciones de settings por default
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Shueisha.settings")

#Acceso a la aplicación
application = get_wsgi_application()