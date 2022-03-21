def formata_preco(val):
    a = 'R$ {:,.2f}'.format(float(val))
    b = a.replace(',','a')
    c = b.replace('.',',')
    return (c.replace('a','.'))

def cart_qtd(cart):
    return sum([item['quantidade'] for item in cart.values()])

def cart_total(cart):
    return sum(
        [
            item.get('preco_quantitativo_promocional')
            if item.get('preco_quantitativo_promocional')
            else item.get('preco_quantitativo')
            for item 
            in cart.values()
        ]
    )
