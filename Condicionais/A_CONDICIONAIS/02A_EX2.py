#2. Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.

def main ():
    n1 = input('Insira o número 1: ')
    n2 = input('Insira o número 2: ')
    verificar(n1,n2)


def verificar(n1,n2):
    if n1 > n2:
        print (f'{n1} é maior que {n2}')
    elif n2 > n1:
        print (f'{n2} é maior que {n1}')
    else:
        print('Os dois são iguais')

main()