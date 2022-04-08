from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('propietarios/', views.propietarios),
    path('nuevoP/', views.nuevoP),
    path('eliminarP/<id>', views.eliminarP),
    path('edicionP/<id>', views.edicionP),
    path('editarP/', views.editarP),
    path('mascotas/', views.mascotas),
    path('nuevaM/', views.nuevaM),
    path('eliminarM/<id>', views.eliminarM),
    path('edicionM/<id>', views.edicionM),
    path('editarM/', views.editarM)
]