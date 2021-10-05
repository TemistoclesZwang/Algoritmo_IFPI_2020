# Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.

n = int(input('Digite o valor de n: '))
soma = 0

for numero in range(1, n+1):
   soma += numero

if numero == n:
   print(soma)
