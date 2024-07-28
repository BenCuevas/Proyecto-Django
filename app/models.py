from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    stock = models.IntegerField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)
    

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre