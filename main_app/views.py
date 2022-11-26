from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    return render(request, "index.html")

def Registrarse2(request):
    form = forms.UserRegisterForm()
    data = {'form':form}
    return render(request, "iniciar_sesion.html", data)

def Registrarse(request):
    form = forms.UserRegisterForm()

    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            print("Form is valid!")
            print("Nombre: ", form.cleaned_data['nombre'])
            print("Apellido: ", form.cleaned_data['apellido'])
            print("Correo: ", form.cleaned_data['email'])
            print("Contraseña: ", form.cleaned_data['contrasenia'])


    data = {'form':form}
    return render(request, "iniciar_sesion.html", data)

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
