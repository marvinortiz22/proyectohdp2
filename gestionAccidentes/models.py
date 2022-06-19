from django.db import models
from django.contrib.auth.models import User
from .choices import Departamentos

class ReporteAccidente(models.Model):
    departamento=models.CharField(max_length=20)
    municipio=models.CharField(max_length=30)
    lugar=models.CharField(max_length=50)    
    descripcion=models.CharField(max_length=100)
    latitud=models.CharField(max_length=50)
    longitud=models.CharField(max_length=50)   
    fecha=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.nombre

class DatosExtra(models.Model):
    cantVictimas=models.IntegerField(blank=True,null=True, verbose_name="Cantidad de victimas")
    foto=models.ImageField(upload_to ='images',blank=True,null=True)
    accidente=models.ForeignKey(ReporteAccidente, on_delete=models.CASCADE)
    
class Reporte(models.Model):
    accidente=models.ForeignKey(ReporteAccidente, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

