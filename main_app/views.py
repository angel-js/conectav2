from django.shortcuts import render, redirect
from . import forms
from .models import Comentario

# Create your views here.
def home(request):
    return render(request, "index.html")

# Guia
def UserRegistrationView(request):
    form = forms.UserRegisterForm()
    
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            print("Form is valid!")
            print("Nombre: ", form.cleaned_data['nombre'])
            print("Apellido: ", form.cleaned_data['apellido'])
            print("Correo: ", form.cleaned_data['email'])
            print("Contraseña: ", form.cleaned_data['contrasenia'])

    data = {'form': form}
    return render(request, 'sesion/userRegistration.html', data)
# Fin Registro

def IniciarSesion(request):
    return render(request, 'sesion/iniciar_sesion.html')

def FichaView(request):
    return render(request, 'ficha/fichaPaciente.html')

# COmentarios
def listarComentarios(request):
    comentarios = Comentario.objects.all()
    data = {'comentarios': comentarios}
    return render(request, 'comentario/comentarios.html', data)

def agregarComentario(request):
    form = forms.FormComentario()
    if request.method == 'POST':
        form = forms.FormComentario(request.POST)
        if form.is_valid():
            form.save()
        return redirect("./../ficha")
    data = {'form': form}
    return render(request, 'comentario/agregarComentario.html', data)