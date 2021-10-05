# 3 Leia N e escreva todos os números inteiros pares de 1 a N.


def ler_n():
   contador = 0
   n = int(input('Digite um número: '))
   
   while contador < n:
      contador += 1

      if (contador % 2) == 0:
         print(f'{contador} É par')


ler_n()


