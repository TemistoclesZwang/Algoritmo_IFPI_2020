#Leia uma matriz quadrada de ordem N e encontre a linha que possui a maior e a menor soma dos elementos.


matriz_geral = []

def gerar_matriz():
   import random
   global matriz_geral
   quantidade_numeros = int(input('Digite a quantidade de elementos que a matriz TERÁ (não confundir com os números que componhem a matriz): '))

   contador_geral = 0
   contador = 0

   matriz = []
   calculo_linhas = (quantidade_numeros * quantidade_numeros) + quantidade_numeros


   while contador_geral < calculo_linhas:
      gerar_numero = random.randint (1,100000)
      contador += 1
      contador_geral += 1
      
      if contador <= quantidade_numeros:
         matriz.append(gerar_numero)
      
      elif contador >= quantidade_numeros:
         matriz_geral.append(matriz)
         contador = 0
         matriz = []   


def imprimir ():
   global matriz_geral
   for linha in matriz_geral:
      print(linha)
   print('\n')
   

def maior_menor():
   global matriz_geral
   linha = 0
   soma = 0
   lista_organizar_somas = []

   while linha < len(matriz_geral):
      for numero in matriz_geral[linha]:
         soma += numero
      lista_organizar_somas.append(soma)
      linha += 1
      ordenar = sorted(lista_organizar_somas, reverse=True)
      
      print(f'Linha{linha} Soma: {soma}') 
   print('\n')
   print(f'Maior soma: {ordenar[0]} Menor soma: {ordenar[-1]}')


gerar_matriz()
imprimir ()
maior_menor()
