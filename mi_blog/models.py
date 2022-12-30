from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=75)
    sub_titulo = models.CharField(max_length=75)
    texto = models.TextField(max_length=3000)
    imagen = models.ImageField(upload_to='posteos', null='True', blank=True)
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

class Avatar(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='avatar')
    imagen = models.ImageField(upload_to='avatares', null='True', blank=True)

class Mensaje(models.Model):
    email = models.EmailField()
    nombre = models.CharField(max_length=50)
    texto = models.TextField(max_length=1000)
    enviado_el = models.DateField(auto_now_add=True)