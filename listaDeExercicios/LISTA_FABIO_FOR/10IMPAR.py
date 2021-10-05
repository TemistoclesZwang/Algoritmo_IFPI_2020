# Leia LimiteSuperior e LimiteInferior e escreva todos os números ímpares entre os limites lidos.
limite_inferior = int(input('Digite o valor inicial: '))
limite_superior = int(input('Digite o valor limite: '))

for numero in range(limite_inferior, limite_superior + 1):
   if not numero % 2 == 0:
      print(f'{numero} é impar')