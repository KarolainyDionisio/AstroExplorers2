from django.urls import path
from .views import IndexView, CatalogoView, ForumView, LojaView, CadastroView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  
    path('catalogo.html', CatalogoView.as_view(), name='catalogo'), 
    path('forum.html', ForumView.as_view(), name='forum'),  
    path('loja.html', LojaView.as_view(), name='loja'), 
    path('cadastro..html', CadastroView.as_view(), name='cadastro'),
]
