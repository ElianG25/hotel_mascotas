from django.shortcuts import redirect, render
from .models import Propietario, Mascota, Aulas, Servicios

# Create your views here.


def home(request):
    return render(request, "index.html")


def propietarios(request):
    servs = Servicios.objects.all()
    habs = Aulas.objects.all()
    mascs = Mascota.objects.all()
    props = Propietario.objects.all()
    return render(request, "propietarios.html", {"props": props, "mascs": mascs, "habs": habs, "servs": servs})


def mascotas(request):
    servs = Servicios.objects.all()
    habs = Aulas.objects.all()
    mascs = Mascota.objects.all()
    props = Propietario.objects.all()
    return render(request, "mascotas.html", {"props": props, "mascs": mascs, "habs": habs, "servs": servs})


def nuevaM(request):
    nombre = request.POST['nombre']
    sexo = request.POST['sexo']
    categoria = request.POST['categoria']
    raza = request.POST['raza']
    fecha_entrada = request.POST['fecha_entrada']
    fecha_salida = request.POST['fecha_salida']
    aula = request.POST['aula']
    propietario = request.POST['propietario']
    servicio = request.POST['servicio']

    mascota = Mascota.objects.create(
        nombre=nombre, sexo=sexo, categoria=categoria, raza=raza, fecha_entrada=fecha_entrada, fecha_salida=fecha_salida, aulas=aula, propietarios=propietario, servicios=servicio
    )

    return redirect('/mascotas')

def eliminarM(request, id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()

    return redirect('/mascotas')

def editarM(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    sexo = request.POST['sexo']
    categoria = request.POST['categoria']
    raza = request.POST['raza']
    fecha_entrada = request.POST['fecha_entrada']
    fecha_salida = request.POST['fecha_salida']
    aula = request.POST['aula']
    propietario = request.POST['propietario']
    servicio = request.POST['servicio']

    mascota = Mascota.objects.get(id=id)
    mascota.nombre = nombre
    mascota.sexo = sexo
    mascota.categoria = categoria
    mascota.raza = raza
    mascota.fecha_entrada = fecha_entrada
    mascota.fecha_salida = fecha_salida
    mascota.aula = aula
    mascota.propietario = propietario
    mascota.servicio = servicio
    mascota.save()

    return redirect('/mascotas')


def edicionM(request, id):
    servs = Servicios.objects.all()
    habs = Aulas.objects.all()
    mascs = Mascota.objects.all()
    props = Propietario.objects.all()
    mascota = Mascota.objects.get(id=id)
    return render(request, "edicionM.html", {"props": props, "mascota": mascota, "habs": habs, "servs": servs, "props": props})

def nuevoP(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']

    propietario = Propietario.objects.create(
        nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono
    )

    return redirect('/propietarios')


def eliminarP(request, id):
    propietario = Propietario.objects.get(id=id)
    propietario.delete()

    return redirect('/propietarios')


def editarP(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']

    propietario = Propietario.objects.get(id=id)
    propietario.nombre = nombre
    propietario.apellido = apellido
    propietario.direccion = direccion
    propietario.telefono = telefono
    propietario.save()

    return redirect('/propietarios')


def edicionP(request, id):
    servs = Servicios.objects.all()
    habs = Aulas.objects.all()
    mascs = Mascota.objects.all()
    props = Propietario.objects.all()
    propietario = Propietario.objects.get(id=id)
    return render(request, "edicionP.html", {"props": props, "mascs": mascs, "habs": habs, "servs": servs, "propietario": propietario})
