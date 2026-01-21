from django.shortcuts import render, get_object_or_404
from .models import Livro

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, "biblioteca/listar_livros.html", {"livros": livros})

def detalhes_livro(request, id):
    livro = Livro.objects.get(id=id)
    return render(request, "biblioteca/detalhe_livro.html", {"livro": livro})