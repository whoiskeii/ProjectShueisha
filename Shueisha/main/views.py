#"Views.py" se encarga de crear las vistas en donde se vizualizará toda la información que se encuentra dentro de los templates/htmls

#Imports necesarios para el correcto funcionamiento de la página web
from distutils.command.upload import upload
from django.shortcuts import render
from django.contrib import messages

#Se importan los modelos creados en "models.py"
from .models import (
    blog,
    categorie,
    detail,
    review,
    watching,
    detail
)

from  django.views import generic

#Se importan los formularios creados en "forms.py"
from . forms import ContactForm, ReviewForm, CreateUserForm

#Imports necesarios para el inicio de sesión de un usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect #Redirecciona a la página web

#Función para el registro del usuario
def registerPage(request):
	if request.user.is_authenticated: #Si el usuario está autenticado/logeado
		return redirect("main:home") #Redirecciona al "inicio" de la página web
	else: #En caso de que el usuario no esté logeado
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid(): #Si es válido
				form.save() #Guarda la información
				user = form.cleaned_data.get('username') #Limpia el form del "username"
				messages.success(request, 'La cuenta fue creada para ' + user) #Confirma la creación del usuario

				return redirect('main:login') #Luego, redirecciona a la página de "login"
			

		context = {'form':form}
		return render(request, 'main/register.html', context)

#Función para el unicio de sesión del usuario
def loginPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		if request.method == 'POST':
			username = request.POST.get('username') #Pide el "username y password"
			password =request.POST.get('password')

            #Autentica si existe y coincide
			user = authenticate(request, username=username, password=password)

            #Si el usuario existe correctamente
			if user is not None:
				login(request, user)
				return redirect("main:home") #Envía al "inicio" de la página web
			else: #En caso de que no sea así
				messages.info(request, 'Nombre de usuario o contraseña incorrecta') #Se encarga de enviar este mensaje

		context = {}
		return render(request, 'main/login.html', context)

#Función para el cierre de sesión del usuario (se utiliza una función ya existente)
def logoutUser(request):
	logout(request)
	return redirect('main:login')

#Creación de la clase o vista llamada "IndexView"
class IndexView(generic.TemplateView):
    template_name = "main/index.html" #El inicio se hace visible por medio del html de "index"

    def get_context_data(self, **kwargs): #Obtiene la data
        context = super().get_context_data(**kwargs) #Recoje la información

        blogs = blog.objects.filter(is_active=True) #Indica si se encuentra activo
        reviews = review.objects.filter(is_active=True)

        context["blogs"] = blogs #Lo que se pide en la base de datos, guardado en una variable, para poder guardarse en "context"
        context["reviews"] = reviews
        return context

#Creación de la clase o vista llamada "BlogView"
class BlogView(generic.ListView): #Solo muestra ciertas entradas, y luego del click, se expande la información
    model = blog
    template_name = "main/blog.html" #El blog de la empresa Shueisha se hace visible por medio del html de "blog"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active = True) #Se realiza un "return", y el "super" es un filtro para que solo se acceda una información específica

#Creación de la clase o vista llamada "BlogDetailView"
class BlogDetailView(generic.DetailView):
    model = blog
    template_name = "main/blog-details.html"

#Creación de la clase o vista llamada "ReviewView"
class ReviewView(generic.ListView):
    model = review
    template_name = "main/anime-details.html" #Los reviews a detalle se hacen visible por medio del html de "anime-details"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active = True)

#Creación de la clase o vista llamada "ReviewDetailView"
class ReviewDetailView(generic.DetailView):
    model = review
    template_name = "main/anime-watching.html"

#Creación de la clase o vista llamada "CategorieView"
class CategorieView(generic.ListView):
    model = categorie
    template_name = "main/categories.html" #Las categorías de animes y mangas se hacen visible por medio del html de "categories"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active = True)

#Creación de la clase o vista llamada "WatchingView"
class WatchingView(generic.ListView):
    model = watching
    template_name = "main/anime-watching.html" #Los animes vistos se hacen visible por medio del html de "anime-watching"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active = True)

#Creación de la clase o vista llamada "DetailView"
class DetailView(generic.ListView):
    model = detail
    template_name = "main/blog-details.html" #El blog a detalle se hace visible por medio del html de "blog-details"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active = True)

#Creación de la clase o vista llamada "ContactView"
class ContactView(generic.FormView):
    template_name = "main/contact.html" #La creación de un blog se hace visible por medio del html de "contact"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()

        #Mensaje que se despliega al momento de realizar la acción
        messages.success(self.request, '¡Gracias por querer formar parte de nuestro sitio web! Estaremos leyendo todos tus comentarios.')
        return super().form_valid(form)

#Creación de la clase o vista llamada "UserReviewView"
class UserReviewView(generic.FormView):
    template_name = "main/upload.html" #La creación de un review se hace visible por medio del html de "upload"
    form_class = ReviewForm
    success_url = "/"

    def form_valid(self, form):
        form.save()

        #Mensaje que se despliega al momento de realizar la acción
        messages.success(self.request, '¡Gracias por querer formar parte de nuestro sitio web! Estaremos leyendo todos tus comentarios.')
        return super().form_valid(form)