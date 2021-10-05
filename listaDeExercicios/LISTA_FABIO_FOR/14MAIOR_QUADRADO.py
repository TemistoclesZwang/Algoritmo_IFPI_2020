# Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o
# maior quadrado menor que 38 é 36 (quadrado de 6).


n = int(input('Informe o valor de N: '))
calc_anterior = 0

for numero in range(1, n + 1):

   calc = numero ** 2

   if calc < n + 1:
      calc_anterior = calc
   else:
      print(calc_anterior)
      break