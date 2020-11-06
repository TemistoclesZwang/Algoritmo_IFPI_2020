# 6. Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
# se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180o). Se formam,
# verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo (1 ângulo = 90o) ou
# obtusângulo (1 ângulo > 90o). Não existe ângulo com tamanho 0o (zero grau).


def main():
    n1 = int(input('Insira o número 1: '))
    n2 = int(input('Insira o número 2: '))
    n3 = int(input('Insira o número 3: '))
    verificar(n1, n2, n3)


def verificar(n1, n2, n3):
    soma = n1 + n2 + n3
    
    if soma == 180 and n1 and n2 and n3 < 90:
        print('Formam um triângulo acutângulo.')

    elif soma == 180 and n1 or n2 or n3 == 90:
        print('Formam um retângulo.')

    elif soma == 180 and n1 or n2 or n3 > 90:
        print('Formam um obtusângulo.')


main()
