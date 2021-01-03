from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',home , name = "index"),
    path('generales/',generales, name = "generales"),
    path('programacion/',programacion, name = "programacion"),
    path('videojuegos/',videojuegos, name = "videojuegos"),
    path('tutoriales/',tutoriales, name = "tutoriales"),   
    path('deportes/',deportes, name = "deporte"),   

    path('?P<slug>[-\w]+)/$',detallepost, name = "detalle_post"),
    ]
    