from django.shortcuts import render, get_object_or_404, redirect

from galeria.models import Thumb

from django.contrib import messages 

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa logar para fazer isso!")
        return redirect('login')

    fotosthumb = Thumb.objects.order_by("nome").filter(publicada=True)

    return render(request, 'galeria/index.html', {"cards": fotosthumb})

def imagem(request, foto_id):
    fotocapa = get_object_or_404(Thumb, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotocapa": fotocapa})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa logar para fazer isso!")
        return redirect('login')


    fotosthumb = Thumb.objects.order_by("nome").filter(publicada=True)
    if "buscar" in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            fotosthumb = fotosthumb.filter(nome__icontains=nome_buscar)

    return render(request, "galeria/buscar.html", {"cards":fotosthumb })