#"Urls.py" se encarga de crear la lista de "urlpatterns"

#Import necesario para el correcto funcionamiento de la página web
from django.urls import path

#Solo los usuarios que están logeados, pueden acceder a las secciones permitidas
from django.contrib.auth.decorators import login_required 

#Se importan los vistas creadas en "views.py"
from . import views

#Nombre de la aplicación
app_name = 'main'

#Direcciones urls que se encargan de hacer visible la vista de cada html
urlpatterns= [
    path('register/', views.registerPage, name="register"),
	path('accounts/login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
    
    path('', views.IndexView.as_view(), name='home'),
    path('blog/', views.BlogView.as_view(), name='blogs'),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name='blog'),
    path('review/', views.ReviewView.as_view(), name='reviews'),
    path('review/<slug:slug>', views.ReviewDetailView.as_view(), name='review'),
    path('index.html', views.IndexView.as_view(), name='home'),
    path('categories.html/', views.CategorieView.as_view(), name='categorie'),
    path('anime-watching.html/', views.WatchingView.as_view(), name='watching'),
    path('blog-details.html/', views.DetailView.as_view(), name='detail'),
    path('contact/', login_required(views.ContactView.as_view()), name="contact"),
    path('upload/', login_required(views.UserReviewView.as_view()), name="upload"),
]