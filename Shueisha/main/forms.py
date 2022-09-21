#"Forms.py" se encarga de crear los formularios en donde se almacenará la información dentro de la página admin de django

#Imports necesarios para el correcto funcionamiento de la página web
from dataclasses import field
from email import message
from email.mime import image
from pyexpat import model
from tkinter import Widget
from django import forms

#Se importan los modelos creados en "models.py"
from .models import ContactProfile
from .models import UserReview

#Imports necesarios para la creación del usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Creación de la clase o formulario llamado "ContactForm"
class ContactForm(forms.ModelForm):

    #Se encarga de mostrar un texto de espera según el campo a llenar
    #Campo con el espacio para ingresar el nombre completo
    name = forms.CharField(max_length=100, required=True, #Indica si el campo es requerido u obligatorio
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre...', 
            }))

    #Campo con el espacio para ingresar el email
    email = forms.EmailField(max_length=254, required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Email...', #"EmailField" válida que se introduzca un correo correctamente
            }))

    #Campo con el espacio para ingresar el título del blog
    title = forms.CharField(max_length=1000, required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Título...',
            }))

    #Campo con el espacio para ingresar el mensaje o comentario deseado
    message = forms.CharField(max_length=1000, required=True, 
        widget=forms.Textarea(attrs={
            'placeholder': 'Mensaje...',
            'row': 6, #Cantidad de líneas para escribir el texto
            }))

    #Campo para adjuntar imagen relacionada
    image = forms.ImageField()

    #Clase "Meta" que indica en donde se guardará la información introducida
    class Meta:

        #Modelo en donde se almacenará la información
        model = ContactProfile

        #Dichos campos a almacenar la información recibida
        fields = ('name', 'email', 'title', 'message', 'image')


#Creación de la clase o formulario llamado "ReviewForm"
class ReviewForm(forms.ModelForm):

    #Se encarga de mostrar un texto de espera según el campo a llenar
    #Campo con el espacio para ingresar el nombre completo
    name = forms.CharField(max_length=100, required=True, #Indica si el campo es requerido u obligatorio
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre...', 
            }))

    #Campo con el espacio para ingresar el email
    email = forms.EmailField(max_length=254, required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Email...', #"EmailField" válida que se introduzca un correo correctamente
            }))
    
    #Campo con el espacio para ingresar el título del review
    title = forms.CharField(max_length=1000, required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Título...',
            }))
    
    #Campo con el espacio para ingresar el mensaje o comentario deseado
    message = forms.CharField(max_length=1000, required=True, 
        widget=forms.Textarea(attrs={
            'placeholder': 'Mensaje...',
            'row': 6, #Cantidad de líneas para escribir el texto
            }))
    
    #Campo para adjuntar imagen relacionada
    image = forms.ImageField()

    #Clase "Meta" que indica en donde se guardará la información introducida
    class Meta:

        #Modelo en donde se almacenará la información
        model = UserReview

        #Dichos campos a almacenar la información recibida
        fields = ('name', 'email', 'title', 'message', 'image')

#Creación de la clase o formulario llamado "CreateUserForm"
class CreateUserForm(UserCreationForm):

    #Clase "Meta" que indica en donde se guardará la información introducida
	class Meta:

        #Modelo en donde se almacenará la información (viene por defecto)
		model = User

        #Dichos campos a almacenar la información recibida
		fields = ['username','email','password1','password2']