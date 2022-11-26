from django import forms 
from django.core import validators
from .models import Comentario

# Registro
class UserRegisterForm(forms.Form):

    ESTADOS = [('activo', 'ACTIVO'), ('inactivo', 'INACTIVO')]

    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25),
    ])
    apellido = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(35),
    ])
    email = forms.CharField()
    contrasenia = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    contrasenia.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'

    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@') == -1:
            raise forms.ValidationError('El correo debe contener @')
        return inputEmail
# Fin registro

#Comentario
class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'