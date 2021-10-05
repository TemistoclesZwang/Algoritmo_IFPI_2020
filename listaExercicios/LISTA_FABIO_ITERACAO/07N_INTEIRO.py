# Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.



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
   print(soma)

ler_n()

