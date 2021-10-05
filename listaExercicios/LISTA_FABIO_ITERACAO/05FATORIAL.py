# Leia um número, calcule e escreva seu fatorial.


def ler_n():
   fator = 1
   contador = 1

   numero = int(input('Digite o valor limite: '))
   print(f'O fatorial de {numero} é:')
   
   while contador <= numero:
      fator *= contador
      contador += 1
      print(fator)


ler_n()