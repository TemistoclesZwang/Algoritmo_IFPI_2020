# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Geométrica que tem por valor inicial A0 e razão R.


def ler_n():
   contador = 1

   A0 = int(input('Digite o valor inicial: '))
   Limite = int(input('Digite o valor limite: '))
   R = int(input('Digite a razão: '))
   
   while contador < Limite:
      contador += 1
      calc = A0 * R **(contador -1)
      print(calc)


ler_n()

