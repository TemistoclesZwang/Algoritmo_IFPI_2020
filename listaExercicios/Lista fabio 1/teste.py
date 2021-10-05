import math

numero = int(input('Digite um número: '))
if ((math.factorial(numero-1)) + 1) % numero == 0:
    print('É primo')
else:
    print('Não é primo')
