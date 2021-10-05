# Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.

n = int(input('Digite o valor de N: '))
contador = 0
lista = []
soma = 0

for numero in range(1, n + 1):
   contador = numero
   lista.append(contador)

for numero in range(len(lista)):
   soma += lista[numero]
   media = soma / len(lista)

print(f'Soma: {soma}')
print(f'Média: {media}')
