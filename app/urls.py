from django.urls import path
from .views import *
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('estrelas/', EstrelaListView.as_view(), name='estrelas'),
    path('estrela/<int:pk>/', EstrelaDetailView.as_view(), name='estrela_detail'),
    path('forum/', TopicoListView.as_view(), name='forum'),
    path('forum/<int:pk>/', TopicoDetailView.as_view(), name='topico_detail'),
    path('constelacoes/', ConstelacaoListView.as_view(), name='constelacoes'),
    path('constelacao/<int:pk>/', ConstelacaoDetailView.as_view(), name='constelacao_detail'),
    path('pesquisa/', PesquisaView.as_view(), name='pesquisa'),
    path('loja/', ProdutoListView.as_view(), name='loja'),
    path('carrinho/', CarrinhoView.as_view(), name='carrinho'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('confirmacao/', ConfirmacaoView.as_view(), name='confirmacao'),
]