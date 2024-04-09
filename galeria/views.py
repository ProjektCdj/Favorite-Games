from django.shortcuts import render



def index(request):


    dados = {
        1: {"nome": "Monster Hunter",
            "plataforma": "PS4 / PC / SWITCH "},
        2: {"nome": "Satisfactory",
            "plataforma": "PC"}
    }


    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')