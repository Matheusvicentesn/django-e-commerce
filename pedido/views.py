import imp
from urllib import request
from django.shortcuts import render, redirect, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from produto.models import Variacao
from utils import utils
from .models import Pedido, ItemPedido

 
class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:criar')

        return super().dispatch(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(usuario=self.request.user)
        return qs


class Pagar(DispatchLoginRequiredMixin, DetailView):
    template_name = 'pedido/pagar.html'
    model = Pedido
    pk_url_kwarg = 'pk'
    context_object_name = 'pedido'


class SalvarPedido(View):
    template_name = 'pedido/pagar.html'

    def get(self, *args, **kwargs):

        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'Você precisa realizar login'
            )
            return redirect('perfil:criar')

        if not self.request.session.get('cart'):
            messages.error(
                self.request,
                'Carrinho Vazio'
            )
            return redirect('produto:lista')

        cart = self.request.session.get('cart')
        cart_variacao_ids = [v for v in cart]
        bd_variacoes = list(Variacao.objects.select_related(
            'produto').filter(id__in=cart_variacao_ids))
        print(bd_variacoes)

        for variacao in bd_variacoes:
            vid = str(variacao.id)
            estoque = variacao.estoque
            qntd_cart = cart[vid]['quantidade']
            preco = cart[vid]['preco']
            preco_promo = cart[vid]['preco_promocional']

            error_msg_estoque = ''

            if estoque < qntd_cart:
                cart[vid]['quantidade'] = estoque
                cart[vid]['preco_quantitativo'] = estoque * preco
                cart[vid]['preco_quantitativo_promocional'] = estoque * \
                    preco_promo

                error_msg_estoque = 'Estoque insuficiente para alguns dos \
                    produtos no seu carrinho Reduzimos a quantidade desses  \
                    produtos. Verifique quais produtos foram afetados no seu \
                    carrinho'
                if error_msg_estoque:
                    messages.error(
                        self.request,
                        error_msg_estoque
                    )
                self.request.session.save()
                return redirect('produto:cart')

        qtd_total_cart = utils.cart_qtd(cart)
        valor_total_cart = utils.cart_total(cart)

        pedido = Pedido(
            usuario=self.request.user,
            total=valor_total_cart,
            qtd_total=qtd_total_cart,
            status='C',

        )

        pedido.save()

        ItemPedido.objects.bulk_create(
           [
               ItemPedido(
                    pedido = pedido,
                    produto = v['produto_nome'],
                    produto_id = v['produto_id'],
                    variacao = v['variacao_nome'],
                    variacao_id = v['variacao_id'],
                    preco = v['preco_quantitativo'],
                    preco_promocional = v['preco_quantitativo_promocional'],
                    quantidade = v['quantidade'],
                    imagem = v['imagem'],
               ) for v in cart.values()
           ]
        )

        del self.request.session['cart']
        return redirect(
            reverse(
                'pedido:pagar',
                kwargs={'pk': pedido.pk}
            )
        )


class Detalhe(DispatchLoginRequiredMixin, DetailView):
    model = Pedido
    context_object_name = 'pedido'
    template_name = 'pedido/detalhe.html'
    pk_url_kwarg = 'pk'



class Lista(DispatchLoginRequiredMixin ,ListView):
    model = Pedido
    context_object_name = 'pedidos'
    template_name = 'pedido/lista.html'
    paginate_by = 10
    ordering = ['-id']
