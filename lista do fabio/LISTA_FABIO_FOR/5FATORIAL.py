# Leia um número, calcule e escreva seu fatorial.

def ler_n():
   fator = 1
   limite = int(input('Digite o valor limite: '))
   print(f'O fatorial de {limite} é:')
   
   for numero in range (1, limite):
      fator *= numero
      print(fator)


ler_n()