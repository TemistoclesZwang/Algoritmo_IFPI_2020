#Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.

def main():
   n = int(input('Número N: '))
   LimiteInferior = int(input('Digite o limite inferior: '))
   LimiteSuperior = int(input('Digite o limite superior: '))

   while LimiteInferior <= LimiteSuperior:
      if LimiteInferior % n == 0:
         print(LimiteInferior)

      LimiteInferior += 1


main()


