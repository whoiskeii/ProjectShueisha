#"Models.py" se encarga de crear las tablas o modelos en donde se almacenará la información de la base de datos dentro de la página admin de django

#Imports necesarios para el correcto funcionamiento de la página web
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

#Creación de la clase, tabla o modelo llamado "blog", en el cual se manejará la información contenida en los blogs de la empresa Shueisha
class blog(models.Model):

    #Clase "Meta" que indica los nombres con los que cuenta dicho modelo
    class Meta:
        verbose_name_plural = 'Shueisha Blogs'
        verbose_name = 'Shueisha Blog'
        ordering = ["timestamp"] #Como se ordena la información ingresada

    #Declaración de los campos con los que contará la tabla en la base de datos
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog") #Señaliza en donde se debe subir/guardar la imagen
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

#Creación de la clase, tabla o modelo llamado "review", en el cual se manejará la información contenida en los reviews de la empresa Shueisha
class review(models.Model):

    #Clase "Meta" que indica los nombres con los que cuenta dicho modelo
    class Meta:
        verbose_name_plural = 'Shueisha Reviews'
        verbose_name = 'Shueisha Review'
        ordering = ["timestamp"]

    #Declaración de los campos con los que contará la tabla en la base de datos
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="review")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(review, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/review/{self.slug}"

#Creación de la clase, tabla o modelo llamado "categorie"
class categorie(models.Model):

    #Clase "Meta" que indica los nombres con los que cuenta dicho modelo
    class Meta:
        verbose_name_plural = 'categories'
        verbose_name = 'categorie'
        ordering = ["timestamp"]

    #Declaración de los campos con los que contará la tabla en la base de datos
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="categorie")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(categorie, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/categorie/{self.slug}"

#Creación de la clase, tabla o modelo llamado "watching"
class watching(models.Model):

    #Clase "Meta" que indica los nombres con los que cuenta dicho modelo
    class Meta:
        verbose_name_plural = 'watchings'
        verbose_name = 'watching'
        ordering = ["timestamp"]

    #Declaración de los campos con los que contará la tabla en la base de datos
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="watching")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(watching, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/watching/{self.slug}"

#Creación de la clase, tabla o modelo llamado "detail"
class detail(models.Model):

    #Clase "Meta" que indica los nombres con los que cuenta dicho modelo
    class Meta:
        verbose_name_plural = 'details'
        verbose_name = 'detail'
        ordering = ["timestamp"]

    #Declaración de los campos con los que contará la tabla en la base de datos
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="detail")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(detail, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/detail/{self.slug}"

#Creación de la clase, tabla o modelo llamado "ContactProfile", en el cual se manejará la información contenida en los blogs del usuario
class ContactProfile(models.Model):
    
    #Clase "Meta" que indica los nombres con los que cuenta dicho modelo
    class Meta:
        verbose_name_plural = 'User Blogs'
        verbose_name = 'User Blog'
        ordering = ["timestamp"] #Como se ordena la información ingresada
    
    #Declaración de los campos con los que contará la tabla en la base de datos
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    title = models.CharField(verbose_name="Title",max_length=200, blank=True, null=True)
    message = models.TextField(verbose_name="Message")
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="ContactProfile") #Señaliza en donde se debe subir/guardar la imagen
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(ContactProfile, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return f"/contact/{self.slug}"

#Creación de la clase, tabla o modelo llamado "ContactProfile", en el cual se manejará la información contenida en los reviews del usuario
class UserReview(models.Model):
    
    #Clase "Meta" que indica los nombres con los que cuenta dicho modelo
    class Meta:
        verbose_name_plural = 'User Reviews'
        verbose_name = 'User Review'
        ordering = ["timestamp"]
    
    #Declaración de los campos con los que contará la tabla en la base de datos
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    title = models.CharField(verbose_name="Title",max_length=200, blank=True, null=True)
    message = models.TextField(verbose_name="Message")
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="UserReview")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(UserReview, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return f"/upload/{self.slug}"

#Creación de la clase, tabla o modelo llamado "Media", en el cual se manejará todo lo perteneciente a "mediafiles"
class Media(models.Model):

    #Clase "Meta" que indica los nombres con los que cuenta dicho modelo
    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]
	
    #Declaración de los campos con los que contará la tabla en la base de datos
    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)
    def __str__(self):
        return self.name