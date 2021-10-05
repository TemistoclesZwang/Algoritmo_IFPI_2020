# 8. Leia um vetor com N elementos, encontre e escreva o maior e o menor elemento e suas respectivas posições no vetor.

def main():
   entrada = input('Insira a quantidade de elementos (separados por vírgula exemplo 1,2,3,4,5): ').split(',')
   
   inteiros = list(map(int,entrada))
   ordenar = sorted(inteiros, reverse=True)

   posicao_maior = 0
   maior = 0
   
   posicao_menor = 0
   menor = 0

   for numero in inteiros:
      if numero == ordenar [0]:
         maior = numero
         break      
      else:
         posicao_maior += 1


   for numero in inteiros:
      if numero == ordenar[-1]:
         menor = numero
         break
      else:
         posicao_menor +=1

   print(f'Maior número: {maior} posição: {posicao_maior}')
   print(f'Menor número: {menor} posição: {posicao_menor} \n')
   print('--- Lembre que as posições começam em 0 e não em 1 ---')


main()
