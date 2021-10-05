# Leia LimiteSuperior e LimiteInferior e escreva todos os números primos entre os limites lidos.

def ler_n():

   limite_inferior = int(input('Digite o valor inicial: '))
   limite_superior = int(input('Digite o valor limite: '))

   for numero in range (limite_inferior, limite_superior + 1):
      numero += 1

      if numero % 2 == 1:
         print(numero)


ler_n()