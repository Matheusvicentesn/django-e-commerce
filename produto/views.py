from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models

class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 9


class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('DetalheProduto')


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