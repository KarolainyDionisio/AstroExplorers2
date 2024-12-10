from django.contrib import admin
from .models import Galaxia, Constelacao, Perfil, Catalogo, Produto, Forum, Comentario

@admin.register(Galaxia)
class GalaxiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'distancia', 'tipo', 'descricao')  
    search_fields = ('nome', 'descricao', 'tipo')  
    list_filter = ('tipo', 'distancia')  

@admin.register(Constelacao)
class ConstelacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'estrelas_notaveis') 
    search_fields = ('nome', 'descricao') 
    list_filter = ('nome',) 

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'biografia') 
    search_fields = ('usuario__username', 'biografia') 

@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'descricao')  
    search_fields = ('nome', 'descricao', 'tipo')
    list_filter = ('tipo',) 

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'imagem') 
    search_fields = ('nome', 'descricao') 
    list_filter = ('preco',) 

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'texto', 'data_postagem') 
    search_fields = ('usuario__username', 'texto') 
    list_filter = ('data_postagem',) 

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'texto', 'data_postagem', 'galaxia', 'constelacao') 
    search_fields = ('usuario__username', 'texto', 'galaxia__nome', 'constelacao__nome') 
    list_filter = ('data_postagem',) 

