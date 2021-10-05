# Leia LimiteSuperior e LimiteInferior e escreva todos os números ímpares entre os limites lidos.




def ler_n():

   limite_inferior = int(input('Digite o valor inicial: '))
   limite_superior = int(input('Digite o valor limite: '))
   ajuste = limite_inferior - limite_inferior
   
   while ajuste <= limite_superior:
      ajuste += 1
      if ajuste % 2 != 0:
         print(f'{ajuste} é impar')

ler_n()
