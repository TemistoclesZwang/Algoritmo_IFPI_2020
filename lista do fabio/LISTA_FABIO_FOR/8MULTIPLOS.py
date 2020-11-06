# Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.

n = int(input('Número N: '))
LimiteInferior = int(input('Digite o limite inferior: '))
LimiteSuperior = int(input('Digite o limite superior: '))

for numero in range(LimiteInferior, LimiteSuperior + 1):
   if numero % n == 0:
      print(numero)

LimiteInferior += 1
