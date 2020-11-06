# 2. Leia um vetor A com N elementos, verifique e escreva se existem ou não elementos iguais no vetor.

def main():
   vetor_A = input('Insira os elementos do vetor (usando vírgula para separar): ').split(',')

   nao_repete = []
   repete = []

   for numero in vetor_A:
      if numero not in nao_repete:
         nao_repete.append(numero)
         
      else:
         repete.append(numero)

   print(f'Lista dos que não repetem: {nao_repete}')
   print(f'Lista dos que repetem: {repete}')

main()