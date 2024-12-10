from django.contrib.auth.models import User
from django.db import models

class Galaxia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem_url = models.URLField()
    distancia = models.FloatField(help_text="Distância em milhões de anos-luz")
    tipo = models.CharField(max_length=50, choices=[
        ('espiral', 'Espiral'),
        ('eliptica', 'Elíptica'),
        ('irregular', 'Irregular'),
    ], default='espiral')

    def __str__(self):
        return self.nome

class Constelacao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem_url = models.URLField()
    estrelas_notaveis = models.TextField(help_text="Estrelas notáveis dentro da constelação")

    def __str__(self):
        return self.nome


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField(blank=True)
    imagem_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True, default='perfil/default_profile.jpg')

    def __str__(self):
        return f"Perfil de {self.usuario.username}"


class Catalogo(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[
        ('estrela', 'Estrela'),
        ('planeta', 'Planeta'),
        ('galaxia', 'Galáxia'),
        ('constelacao', 'Constelação'),
    ], default='galaxia')
    descricao = models.TextField()
    imagem_url = models.URLField()

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    
    def __str__(self):
        return self.nome


class Forum(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.usuario.username} em {self.data_postagem}"

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    galaxia = models.ForeignKey(Galaxia, null=True, blank=True, on_delete=models.CASCADE)
    constelacao = models.ForeignKey(Constelacao, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.galaxia:
            return f"Comentário sobre {self.galaxia.nome} de {self.usuario.username}"
        elif self.constelacao:
            return f"Comentário sobre {self.constelacao.nome} de {self.usuario.username}"
        return f"Comentário de {self.usuario.username}"
