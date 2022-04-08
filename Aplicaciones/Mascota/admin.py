from django.contrib import admin
from .models import Mascota, Propietario, Aulas, Servicios

# Register your models here.

admin.site.register(Mascota)
admin.site.register(Propietario)
admin.site.register(Aulas)
admin.site.register(Servicios)