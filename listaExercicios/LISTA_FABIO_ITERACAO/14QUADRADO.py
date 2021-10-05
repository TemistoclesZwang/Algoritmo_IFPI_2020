def ler_n():

   n = int(input('Digite: '))
   contador = 0
   calc = 0

   while (contador ** 2) <= n:
      calc = contador ** 2
      contador += 1

   print(f'Maior quadrado menor que {n} é {calc}')

ler_n()

# Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o
# maior quadrado menor que 38 é 36 (quadrado de 6).