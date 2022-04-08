from email.policy import default
from pickle import FALSE
from tabnanny import verbose
from time import time, timezone
from tkinter import CASCADE
from django.db import models

# Create your models here.

SEXO = (
    ('M','Masculino'),
    ('F', 'Femenino'),
)

CATEGORIA = (
    ('canino','Canino'),
    ('felino', 'Felino'),
    ('ave', 'Ave')
)

class Propietario(models.Model):
    nombre=models.CharField(max_length=35, verbose_name='Nombre')
    apellido=models.CharField(max_length=35, verbose_name='Apellido')
    direccion=models.CharField(max_length=100, verbose_name='Direccion')
    telefono=models.CharField(max_length=10, verbose_name='Telefono')

    def nombre_completo(self):
        return "{} {}".format(self.nombre, self.apellido)
    
    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name='Propietario'
        verbose_name_plural='Propietarios'
        db_table='propietarios'

class Aulas(models.Model):
    nombre=models.CharField(max_length=35, verbose_name='Nombre')
    tarifa_por_noche=models.IntegerField(verbose_name='Tarifa por Noche')

    def nombre_completo(self):
        return "{} (${})".format(self.nombre, self.tarifa_por_noche)
    
    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name='Aula'
        verbose_name_plural='Aulas'
        db_table='aulas'

class Servicios(models.Model):
    marca=models.CharField(max_length=50, verbose_name='Marca del Alimento')
    categoria=models.CharField(max_length=15, verbose_name='Categoria del Alimento', choices=CATEGORIA, default='canino')
    nombre_alimento=models.CharField(max_length=50, verbose_name='Nombre del Alimento')
    precio=models.IntegerField(verbose_name='Precio')

    def nombre_completo(self):
        return "{} {} (para {}s) (${})".format(self.marca, self.nombre_alimento, self.categoria, self.precio)
    
    def __str__(self):
        return self.nombre_completo()
    
    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'
        db_table='servicios'

class Mascota(models.Model):
    nombre=models.CharField(max_length=20)
    sexo=models.CharField(max_length=1, choices=SEXO, default='masculino')
    categoria=models.CharField(max_length=15, choices=CATEGORIA, default='canino')
    raza=models.CharField(max_length=30, null=FALSE)
    fecha_entrada=models.DateField(null=FALSE)
    fecha_salida=models.DateField(null=FALSE)
    aula=models.ForeignKey(to=Aulas, null=True, blank=True, on_delete=models.CASCADE)
    servicio=models.ForeignKey(to=Servicios, null=True, blank=True, on_delete=models.CASCADE)
    propietario=models.ForeignKey(to=Propietario, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        text = "{0} ({1} de {2})"
        return text.format(self.nombre, self.raza, self.propietario)

    class Meta:
        db_table='mascotas'
