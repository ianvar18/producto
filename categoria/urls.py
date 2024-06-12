from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('categoria/index', views.index, name='categoria/index'),
]