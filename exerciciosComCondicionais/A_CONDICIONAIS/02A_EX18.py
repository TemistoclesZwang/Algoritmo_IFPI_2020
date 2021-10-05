#18. Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 
# 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa operação
#sobre os dois valores lidos.

def main():
    valor1 = int(input('Insira o valor 1: '))
    valor2 = int(input('Insira o valor 2: '))

    adi(valor1,valor2)
    sub(valor1,valor2)
    mul(valor1,valor2)
    div(valor1,valor2)


def adi(valor1,valor2):
    print (f'A adição dos números é: {valor1+valor2}')

def sub(valor1,valor2):
    if valor1 > valor2:
        print (f'A subtração dos números é {valor1 - valor2}') #Para não ter um output negative
    elif valor2 > valor1:
        print (f'A subtração dos números é {valor2 - valor1}')

def mul(valor1,valor2):
    print (f'A multiplicação dos números é {valor1 * valor2}')

def div(valor1,valor2):
    print (f'A divisão dos números é {valor1 / valor2:.2f}')


main()