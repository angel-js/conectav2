from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('registro/', views.Registrarse,  name="registro"),
    path('registrarse/', views.UserRegistrationView,  name="registrarse"),
]
