# 7. Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3
# (três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se
# formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
# escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).


def main():
    n1 = int(input('Insira o número 1: '))
    n2 = int(input('Insira o número 2: '))
    n3 = int(input('Insira o número 3: '))
    verificar(n1, n2, n3)


def verificar(n1, n2, n3):

    # A soma de dois números não pode ser menor que o terceiro lado
    if n1 + n2 > n3 or n1 + n3 > n2 or n2 + n3 > n1:

        if n1 == n2 or n2 == n3 or n3 == n1:
            if n1 != n2 or n2 != n3 or n3 != n1:  # Se pelo menos um dos lados for diferentes
                print('Dois lados são iguais. É um isósceles')
                pass

        if n1 != n2 and n2 != n3 and n3 != n1:
            print('Os três lados são diferentes. É um escaleno.')
            pass

        if n1 == n2 == n3:
            print('Os três lados são iguais. É um equilátero.')
            pass


main()
