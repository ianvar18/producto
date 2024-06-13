from django.urls import path
from . import views

urlpatterns = [
    path('index', views.lista_servicios, name='lista_servicios'),
    path('nuestros-servicios/', views.nuestros_servicios, name='nuestros_servicios'),
]
