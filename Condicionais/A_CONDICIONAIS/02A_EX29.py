 '''29. Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas
formadas pelos seus dois primeiros e dois últimos dígitos.
Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado perfeito.'''

def main():
    num = int(input('Digite um número: '))
    verificar (num)


def verificar (num):
    raiz = num ** (1 / 2)
    dezena = (num % 100) // 10
    soma_dezena = dezena + dezena

    if raiz == soma_dezena:
        print(f'{num} É um quadrado perfeito')

    elif raiz != soma_dezena:
        print(f'{num} Não é um quadrado perfeito')


main()