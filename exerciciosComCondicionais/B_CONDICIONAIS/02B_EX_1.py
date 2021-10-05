#1Leiaum númeroe mostre na tela se o númeroé positivo ou negativo.

def main():
    num = input('Insira um número: ')
    verificar(num)


def verificar(num):
    if '-' in num:
        print('Esse número é negativo.')
    else:
        print('Esse número é positivo.')


main()