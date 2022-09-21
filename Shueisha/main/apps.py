#Import necesario para el correcto funcionamiento de la página web
from django.apps import AppConfig


#Creación de la clase "MainConfig"
class MainConfig(AppConfig): #Se encarga de crear la aplicación "main"
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"