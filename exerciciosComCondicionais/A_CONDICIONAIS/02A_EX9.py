#9. Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.
import math
numero = int(input('Digite um número entre 0 e 100: '))

if numero == 1:
    print('Não é primo')
elif  ((math.factorial(numero-1)) + 1) % numero == 0:
    print('É primo')
else:
    print('Não é primo')
