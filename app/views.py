from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Galaxia, Constelacao, Produto, Forum, Comentario, Catalogo

class IndexView(TemplateView):
    template_name = 'index.html'

class CatalogoView(TemplateView):
    template_name = 'catalogo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galaxias'] = Galaxia.objects.all()  
        context['constelacoes'] = Constelacao.objects.all()  
        context['produtos'] = Produto.objects.all()  
        context['catalogos'] = Catalogo.objects.all()  
        return context

class ForumView(TemplateView):
    template_name = 'forum.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = Forum.objects.all() 
        return context

class LojaView(TemplateView):
    template_name = 'loja.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()  

class CadastroView(TemplateView):
    template_name = 'cadastro.html'
