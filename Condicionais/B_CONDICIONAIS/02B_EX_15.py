#15


def main():

    morango = float(input('Quantos kg de morango quer comprar?: '))
    maca = float(input('Quantos kg de maçã quer comprar?: '))
    
    if morango <= 5 and maca <= 5:
        menos_5(morango,maca)

    elif morango > 5 and maca > 5:
        mais_5(morango,maca)

    else:
        mais_8(morango,maca)

    

def menos_5(morango,maca):
    moran_preco = 2.5
    maca_preco = 1.80
    
    v_compra = (morango * moran_preco) + (maca * maca_preco)
    print(f'Total a pagar: R$ {v_compra}')
    
def mais_5(morango,maca):
    moran_preco = 2.2
    maca_preco = 1.5

    v_compra = (morango * moran_preco) + (maca * maca_preco)
    print(f'Total a pagar: R$ {v_compra}')

def mais_8(morango,maca):

    moran_preco = 2.2
    maca_preco = 1.5

    v_compra = (morango * moran_preco) + (maca * maca_preco)
    print(f'Total a pagar: R$ {v_compra}')


main()