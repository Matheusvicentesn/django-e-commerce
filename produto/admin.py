from django.contrib import admin
from .models import Produto, Variacao


class VariacaoInLine(admin.TabularInline):
    model = Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco_formatado',
                    'preco_promo_formatado']
    inlines = [
        VariacaoInLine
    ]


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
