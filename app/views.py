from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Estrela, Topico, Constelacao, Produto, Carrinho, Pedido, Pagamento, Pesquisa

# Página Inicial - Exibe produtos mais populares ou recentes
class IndexView(View):
    def get(self, request):
        produtos = Produto.objects.all()  # Exemplo: Todos os produtos
        return render(request, 'index.html', {'produtos': produtos})

    def post(self, request):
        # Caso haja um formulário ou outra interação no POST
        pass


# Catálogo de Estrelas
class EstrelaListView(View):
    def get(self, request):
        estrelas = Estrela.objects.all()  # Busca todas as estrelas
        return render(request, 'estrela_list.html', {'estrelas': estrelas})


class EstrelaDetailView(View):
    def get(self, request, pk):
        estrela = get_object_or_404(Estrela, pk=pk)  # Busca estrela pelo ID
        return render(request, 'estrela_detail.html', {'estrela': estrela})


# Fórum (Listagem de tópicos)
class TopicoListView(View):
    def get(self, request):
        topicos = Topico.objects.all()  # Lista todos os tópicos do fórum
        return render(request, 'forum_list.html', {'topicos': topicos})


class TopicoDetailView(View):
    def get(self, request, pk):
        topico = get_object_or_404(Topico, pk=pk)  # Detalha um tópico específico
        return render(request, 'topico_detail.html', {'topico': topico})


# Constelações
class ConstelacaoListView(View):
    def get(self, request):
        constelacoes = Constelacao.objects.all()  # Lista todas as constelações
        return render(request, 'constelacao_list.html', {'constelacoes': constelacoes})


class ConstelacaoDetailView(View):
    def get(self, request, pk):
        constelacao = get_object_or_404(Constelacao, pk=pk)  # Detalha uma constelação específica
        return render(request, 'constelacao_detail.html', {'constelacao': constelacao})


# Pesquisa (permite que o usuário busque algo)
class PesquisaView(View):
    def get(self, request):
        pesquisa_resultados = None
        termo_busca = request.GET.get('termo', '')  # Pega o termo da query string
        if termo_busca:
            pesquisa_resultados = Pesquisa.objects.filter(termo_busca__icontains=termo_busca)  # Busca na pesquisa
        return render(request, 'pesquisa.html', {'pesquisa_resultados': pesquisa_resultados, 'termo': termo_busca})


# Loja (Listagem de produtos)
class ProdutoListView(View):
    def get(self, request):
        produtos = Produto.objects.all()  # Exibe todos os produtos
        return render(request, 'produto_list.html', {'produtos': produtos})


# Carrinho
class CarrinhoView(View):
    def get(self, request):
        carrinho = Carrinho.objects.filter(usuario=request.user)  # Exibe o carrinho do usuário logado
        return render(request, 'carrinho.html', {'carrinho': carrinho})

    def post(self, request):
        # Se necessário, trate a adição de produtos ao carrinho via POST
        pass


# Checkout (finalização da compra)
class CheckoutView(View):
    def get(self, request):
        carrinho = Carrinho.objects.filter(usuario=request.user)  # Busca o carrinho do usuário
        total = sum(item.produto.preco * item.quantidade for item in carrinho)  # Calcula o total
        return render(request, 'checkout.html', {'carrinho': carrinho, 'total': total})

    def post(self, request):
        # Lógica para processar o pagamento
        carrinho = Carrinho.objects.filter(usuario=request.user)
        total = sum(item.produto.preco * item.quantidade for item in carrinho)
        pedido = Pedido.objects.create(usuario=request.user, total=total, status='Pendente')  # Cria o pedido
        # Aqui você pode adicionar a lógica de pagamento e marcar o pedido como "Pago"
        return render('Pedido realizado com sucesso!')


# Confirmação (após o pagamento ser processado)
class ConfirmacaoView(View):
    def get(self, request):
        # Pode ser implementado para mostrar detalhes do pedido
        return render(request, 'confirmacao.html')
