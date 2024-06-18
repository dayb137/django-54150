from django.db import models

class Paleta(models.Model):
    marca = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)
    fecha = models.DateField()
    
    def __str__(self) -> str:
        return f'{self.marca} {self.fecha}'
    