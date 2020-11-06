# Leia LimiteSuperior e LimiteInferior e escreva todos os números primos entre os limites lidos.


def ler_n():

    limite_inferior = int(input('Digite o valor inicial: '))
    limite_superior = int(input('Digite o valor limite: '))

    while limite_inferior <= limite_superior:
        limite_inferior += 1

        if limite_inferior % 2 == 1:
            print(limite_inferior)


ler_n()
