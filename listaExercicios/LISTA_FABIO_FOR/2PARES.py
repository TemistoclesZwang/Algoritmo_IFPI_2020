# Leia N e escreva todos os números inteiros pares de 1 a N.

n = int(input('Digite o valor de N: '))
n = n + 1

for numero in range(1, n):
   if (numero % 2) == 0:
      print(numero)
   else:
      pass
