from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('registrarse/', views.UserRegistrationView,  name="registrarse"),
    path('iniciar_sesion/', views.UserRegistrationView,  name="iniciar_sesion"),
    path('ficha/', views.FichaView,  name="ficha"),
    path('comentarios/', views.listarComentarios,  name="comentarios"),
    path('agregarComentario/', views.agregarComentario,  name="agregarComentario"),
]
