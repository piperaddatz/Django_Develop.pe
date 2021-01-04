from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator


def home(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    post = Post.objects.filter(estado = True)
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    # paginator = Paginator(post,2)
    # Codigo necesario para saber en que pagina esta:
    # page = request.GET.get('page') 
    # post = paginator.get_page(page)

    return render(request,'index.html', {'posts':post})


def detallepost(request,slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request, 'post.html', {'detalle_post':post})



def generales(request):
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact ='generales'))
    return render(request,'generales.html',{'posts':post})   


def programacion(request):
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact='programacion'))
    return render(request,'programacion.html',{'posts':post})       


def tutoriales(request):
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact="tutoriales"))
    return render(request,'tutoriales.html',{'posts':post})  



def videojuegos(request):
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact='videojuegos'))
    return render(request,'videojuegos.html',{'posts':post})  

def deportes(request):
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact='Deporte'))
    return render(request,'deportes.html',{'posts':post})   