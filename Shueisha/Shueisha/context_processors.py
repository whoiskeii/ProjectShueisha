#"Context_processors.py" se encarga de especificar un número de variables que son incluidas automáticamente en cada contexto

#Imports necesarios para el correcto funcionamiento de la página web
from multiprocessing import context
from django.contrib.auth.models import User

#Función para este
def project_context(request):

    context = {
        'me': User.objects.first(), #Se encarga de mostrar el primer objeto dentro de la clase
    }

    return context