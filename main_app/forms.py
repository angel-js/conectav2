from django import forms 

class UserRegisterForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    contrasenia = forms.CharField()
