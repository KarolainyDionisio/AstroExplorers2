from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relacionamento com o modelo User
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
class Estrela(models.Model):
    nome = models.CharField(max_length=100)
    magnitude = models.FloatField()  # Magnitude da estrela (magnitude aparente)
    tipo_espectral = models.CharField(max_length=20)  # Tipo espectral (ex: G2V, M5III)
    curiosidades = models.TextField(blank=True, null=True)  # Curiosidades sobre a estrela

    def __str__(self):
        return self.nome
    
    class Topico(models.Model):
        titulo = models.CharField(max_length=200)
        autor = models.ForeignKey(User, on_delete=models.CASCADE)
        data_criacao = models.DateTimeField(auto_now_add=True)
        corpo = models.TextField()

    def __str__(self):
        return self.titulo


class Resposta(models.Model):
    topico = models.ForeignKey( on_delete=models.CASCADE, related_name='respostas')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    corpo = models.TextField()

    def __str__(self):
        return f"Resposta de {self.autor.username} em {self.topico.titulo}"

class Constelacao(models.Model):
    nome = models.CharField(max_length=100)
    estrelas_principais = models.ManyToManyField(Estrela, related_name='constelacoes')
    curiosidades = models.TextField(blank=True, null=True)
    localizacao = models.CharField(max_length=100, blank=True, null=True)  # Localização da constelação no céu (coordenadas)

    def __str__(self):
        return self.nome

class Pesquisa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    termo_busca = models.CharField(max_length=255)
    resultado = models.TextField()  # Resultados em formato texto, pode ser expandido para outros tipos

    def __str__(self):
        return f"Pesquisa de {self.usuario.username}: {self.termo_busca}"


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrinho de {self.usuario.username}"

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} no carrinho de {self.carrinho.usuario.username}"


class Pedido(models.Model):
    carrinho = models.OneToOneField(Carrinho, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    endereco_entrega = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('pendente', 'Pendente'), ('enviado', 'Enviado'), ('entregue', 'Entregue')], default='pendente')
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total do pedido

    def __str__(self):
        return f"Pedido {self.id} - {self.status}"

class Pagamento(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    metodo_pagamento = models.CharField(max_length=50, choices=[('cartao', 'Cartão de Crédito'), ('boleto', 'Boleto'), ('paypal', 'PayPal')])
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pagamento do Pedido {self.pedido.id} - {self.metodo_pagamento}"

