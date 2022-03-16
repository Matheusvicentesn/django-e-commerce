from django.template import Library
from utils import utils
register = Library()


@register.filter
def formata_preco(val):
    return utils.formata_preco(val)

@register.filter
def cart_qtd(cart):
    return utils.cart_qtd(cart)

@register.filter
def cart_total(cart):
    return utils.cart_total(cart)