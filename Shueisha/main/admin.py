#"Admin.py" se encarga de crear los usuarios dentro de la página admin de django

#Import necesario para el correcto funcionamiento de la página web
from django.contrib import admin

#Se importan los modelos creados en "models.py"
from . models import (
    blog,
    review,
    ContactProfile,
    UserReview,
    Media,
    )

#Admin creado para almacenar los blogs de la empresa Shueisha
@admin.register(blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active') #Indica si se encuentra activo
    readonly_fields = ('slug',)

#Admin creado para almacenar los reviews de la empresa Shueisha
@admin.register(review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)

#Admin creado para almacenar los blogs del usuario
@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name')
    readonly_fields = ('slug',)

#Admin creado para almacenar los reviews del usuario
@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name')
    readonly_fields = ('slug',)

#Admin creado para almacenar lo perteneciente a "mediafiles"
@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')