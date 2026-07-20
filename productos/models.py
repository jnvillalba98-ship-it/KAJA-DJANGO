from django.db import models


class Producto(models.Model):

    codigo = models.CharField(max_length=20, unique=True)

    nombre = models.CharField(max_length=100)

    descripcion = models.TextField()

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.IntegerField(default=0)

    activo = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre