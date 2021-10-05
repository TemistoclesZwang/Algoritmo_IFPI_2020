# Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...).
n = int(input('Escreva o valor de N: '))
contador = 1
x = 1

for numero in range(1, n + 1, x):
   soma = (numero + 1) + numero
   x = soma
   contador += 1
   
