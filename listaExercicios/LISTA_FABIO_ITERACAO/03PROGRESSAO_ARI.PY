# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Aritmética que tem por valor inicial A0 e razão R.


def ler_n():
   A = int(input('Digite o valor inicial: '))
   Limite = int(input('Digite o valor limite: '))
   R = int(input('Digite a razão: '))
   contador = A
   
   while contador < Limite:
      contador += R
      print(contador)


ler_n()