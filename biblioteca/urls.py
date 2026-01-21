from django.urls import path
from . import views

urlpatterns = [
    path("livros/", views.listar_livros, name="listar_livros"),
    path("livro/<int:id>/", views.detalhes_livro, name="detalhes"),
]