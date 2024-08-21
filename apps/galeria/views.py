from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Thumb
from apps.galeria.forms import ThumbForms
from django.contrib import messages 


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa logar para fazer isso!")
        return redirect('login')

    fotosthumb = Thumb.objects.order_by("nome").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotosthumb})

def imagem(request, foto_id):
    fotosthumb = get_object_or_404(Thumb, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotosthumb": fotosthumb})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa logar para fazer isso!")
        return redirect('login')


    fotosthumb = Thumb.objects.order_by("nome").filter(publicada=True)
    if "buscar" in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            fotosthumb = fotosthumb.filter(nome__icontains=nome_buscar)

    return render(request, "galeria/index.html", {"cards": fotosthumb })

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa logar para fazer isso!")
        return redirect('login')
    
    form = ThumbForms
    if request.method == 'POST':
        form = ThumbForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo Jogo Cadastrado!')
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {'form': form})
    


def editar_imagem(request, foto_id):
    
    
    thumb = Thumb.objects.get(id=foto_id)
    form = ThumbForms(instance=thumb)

    if request.method == 'POST':
        form = ThumbForms(request.POST, request.FILES, instance=thumb)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem Editada.')
            return redirect('index')
        
    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})
    
def deletar_imagem(request, foto_id):
    thumb = Thumb.objects.get(id=foto_id)
    thumb.delete()    
    messages.success(request, 'Jogo Deletado do Catalogo.')
    return redirect('index')

def filtro(request, categoria):
    fotosthumb = Thumb.objects.order_by("nome").filter(publicada=True, categoria=categoria)
    
    return render(request, 'galeria/index.html', {"cards": fotosthumb})