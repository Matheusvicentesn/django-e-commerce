from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from . import models
from pprint import pprint


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 9


class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


class AddToCart(View):
    def get(self, *args, **kwargs):
        #Limpar carrinho
        # if self.request.session.get('cart'):
        #     del self.request.session['cart']
        #     self.request.session.save()

        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista'))
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(
                self.request,
                'Produto inexistente'
            )
            return redirect(http_referer)

        variacao = get_object_or_404(models.Variacao, id=variacao_id)
        variacao_estoque = variacao.estoque
        produto = variacao.produto

        produto_id = produto.id
        produto_nome = produto.nome
        variacao_nome = variacao.nome
        # variacao_id = variacao.id
        preco = variacao.preco
        preco_promocional = variacao.preco_promocional
        # preco_quantitativo
        # preco_quantitativo_promocional
        quantidade = 1
        slug = produto.slug
        imagem = produto.imagem

        if imagem:
            imagem = imagem.name
        else:
            imagem = ''

        if variacao.estoque < 1:
            messages.error(
                self.request,
                'Estoque insuficiente'
            )
            return redirect(http_referer)

        if not self.request.session.get('cart'):
            self.request.session['cart'] = {}
            self.request.session.save()

        cart = self.request.session['cart']

        if variacao_id in cart:
            quantidade_cart = cart[variacao_id]['quantidade']
            quantidade_cart += 1

            if variacao_estoque < quantidade_cart:
                messages.warning(
                    self.request,
                    f'Estoque insuficiente para {quantidade_cart}x no produto'
                    f'"{produto_nome}"'
                )

                quantidade_cart = variacao_estoque

            cart[variacao_id]['quantidade'] = quantidade_cart
            cart[variacao_id]['preco_quantitativo'] = preco * quantidade_cart
            cart[variacao_id]['preco_quantitativo_promocional'] \
                = preco_promocional * quantidade_cart
        else:
            cart[variacao_id] = {
                'produto_id': produto_id,
                'produto_nome': produto_nome,
                'variacao_nome': variacao_nome,
                'variacao_id': variacao_id,
                'preco': preco,
                'preco_promocional': preco_promocional,
                'preco_quantitativo': preco,
                'preco_quantitativo_promocional': preco_promocional,
                'quantidade': 1,
                'slug': slug,
                'imagem': imagem,
            }

        self.request.session.save()
        messages.success(
            self.request,
            f'Produto {produto_nome} {variacao_nome} adicionado ao carrinho'
   
        )
        messages.warning(
            self.request,
            f'Quantidade do produto no seu carrinho: ' \
            f'({cart[variacao_id]["quantidade"]})'

        )


        return redirect(http_referer)


class Remove(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remove')


class Cart(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'produto/cart.html')


class Finish(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finish')
