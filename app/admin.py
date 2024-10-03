from django.contrib import admin
from .models import Perfil, Estrela, Topico, Resposta, Constelacao, Pesquisa, Produto, Carrinho, ItemCarrinho, Pedido, Pagamento

# Registro da model Perfil
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'data_nascimento']
    search_fields = ['user__username', 'bio']
    list_filter = ['data_nascimento']

# Registro da model Estrela
@admin.register(Estrela)
class EstrelaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'magnitude', 'tipo_espectral']
    search_fields = ['nome', 'tipo_espectral']
    list_filter = ['magnitude']

# Registro da model Topico
@admin.register(Topico)
class TopicoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'data_criacao']
    search_fields = ['titulo', 'corpo']
    list_filter = ['data_criacao']

# Registro da model Resposta
@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ['topico', 'autor', 'data_criacao']
    search_fields = ['corpo']
    list_filter = ['data_criacao']

# Registro da model Constelacao
@admin.register(Constelacao)
class ConstelacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'localizacao']
    search_fields = ['nome', 'curiosidades']
    list_filter = ['nome']

# Registro da model Pesquisa
@admin.register(Pesquisa)
class PesquisaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'termo_busca', 'resultado']
    search_fields = ['termo_busca', 'resultado']
    list_filter = ['usuario']

# Registro da model Produto
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'descricao']
    search_fields = ['nome', 'descricao']
    list_filter = ['preco']

# Registro da model Carrinho
@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'criado_em']
    list_filter = ['criado_em']

# Registro da model ItemCarrinho (com Inline)
class ItemCarrinhoInline(admin.TabularInline):
    model = ItemCarrinho
    extra = 1  # Adiciona um formulário vazio extra para criar novos itens no carrinho

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'criado_em']
    inlines = [ItemCarrinhoInline]  # Adiciona o Inline de ItemCarrinho

# Registro da model Pedido
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['carrinho', 'data_pedido', 'status', 'total']
    list_filter = ['status']
    search_fields = ['carrinho__usuario__username', 'status']

# Registro da model Pagamento
@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'metodo_pagamento', 'valor_pago', 'data_pagamento']
    list_filter = ['metodo_pagamento']
    search_fields = ['pedido__carrinho__usuario__username']
