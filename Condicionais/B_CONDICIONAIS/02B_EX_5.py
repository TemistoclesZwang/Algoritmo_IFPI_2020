#Leiao  preço  de  três  produtos  e  informe  qual  produto  deve ser  comprado,  sabendo  que  a  decisão  é sempre pelo mais barato

def main():
    produto1 = input('Insira o valor do produto 1: ')
    produto2 = input('Insira o valor do produto 2: ')
    produto3 = input('Insira o valor do produto 3: ')

    verificar(produto1, produto2, produto3)


def verificar(produto1, produto2, produto3):
    if produto1 < produto2 and produto1 < produto3:
        print ('Compre o produto 1 ele é o mais barato.')

    if produto2 < produto1 and produto2 < produto3:
        print ('Compre o produto 2 ele é o mais barato.')

    if produto3 < produto2 and produto3 < produto1:
        print ('Compre o produto 3 ele é o mais barato.')


main()