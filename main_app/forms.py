from django import forms 
from django.core import validators
from .models import Comentario, Familiar

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

    ESTADOS = [('estable', 'ESTABLE'), ('alerta', 'ALERTA'), ('cuidado intensivo','CUIDADO INTENSIVO')]
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))
    class Meta:
        model = Comentario
        fields = '__all__'

# MI REGISTRO USUARIO
class RegistroFamiliar(forms.ModelForm):
    ESTADOS = [('masculino', 'MASCULINO'), ('femino', 'FEMENINO')]
    ROL = [('familiar', 'FAMILIAR')]
    REGION = [('region metropolitana', 'REGION METROPOLITANA'), ('valparaiso', 'VALPARAISO'), ('coquimbo', 'COQUIMBO'), ('los lagos', 'LOS LAGOS')]
    COMUNAS =[('santiago centro', 'SANTIAGO CENTRO'), ('la reina', 'LA REINA'), ('peñaflor', 'PEÑAFLOR')]
    sexo = forms.CharField(widget=forms.Select(choices=ESTADOS))
    id_rol = forms.CharField(widget=forms.Select(choices=ROL))
    id_region = forms.CharField(widget=forms.Select(choices=REGION))
    id_comuna = forms.CharField(widget=forms.Select(choices=COMUNAS))
    class Meta:
        model = Familiar
        fields = '__all__'