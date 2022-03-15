from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from . import models

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
        return HttpResponse('AddToCart')


class Remove(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remove')


class Cart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Cart')

class Finish(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finish')