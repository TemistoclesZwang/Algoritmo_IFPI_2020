# Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.

def ler_n():
   n = int(input('Digite um numero: '))

   contador1 = 0
   lista = []

   while contador1 < n: 
      contador1 += 1
      lista.append(contador1)

   soma = 0

   for numero in range(len(lista)):
      soma += lista[numero]
      media = soma / len(lista)

   print(f'Soma: {soma}')
   print(f'Média: {media}')
ler_n()