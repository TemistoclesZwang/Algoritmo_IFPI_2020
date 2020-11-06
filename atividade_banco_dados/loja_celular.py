import json
import os
from gerador_banco_dados import gerar_BD

def main():

   if os.path.exists('BD_celulares') == False:
      gerar_BD()
   else:
      #Se já tiver criado o banco de dados antes, não criar de novo
      pass

   entrada()


def entrada():
   opcoes()
   entrada = int(input('Escolha uma opção: '))

   while entrada != 0:
      if entrada == 1:
         mostrar_marcas()
         opcoes()
         entrada = int(input('Escolha uma opção: '))

      elif entrada == 2:
         mostrar_modelos()
         opcoes()
         entrada = int(input('Escolha uma opção: '))

      elif entrada == 3:
         nome_buscado = input('Insira parte do nome do modelo ou marca: ').upper()
         buscar_celular_marca(nome_buscado)
         opcoes()
         entrada = int(input('Escolha uma opção: '))
      
      elif entrada == 4:
         nome_buscado = input('Insira parte do nome do modelo ou marca: ').upper()
         buscar_celular_modelo(nome_buscado)
         opcoes()
         entrada = int(input('Escolha uma opção: '))

      elif entrada == 5:
         if len(posicoes_marca) >= 1:
            entrada_editar_marca(posicoes_marca, posicao_do_cel_escolhido)
         elif len(posicoes_modelo) >= 1:
            entrada_editar_modelo(posicoes_modelo, posicao_do_cel_escolhido)
         #entrada_editar(posicoes_marca,posicoes_modelo,posicao_do_cel_escolhido)
         editar_celular(posicao_do_cel_escolhido)
         # opcoes()
         # entrada = int(input('Escolha uma opção: '))
      
      elif entrada == 0:
         print('Saindo...')

   return nome_buscado


def opcoes():
   opçoes = print(
      '1 Mostrar marcas \n'
      '2 Mostrar modelos \n'
      '3 Buscar celular por marca \n'
      '4 Buscar celular por modelo \n'
      '5 Editar (Faça uma busca antes) \n'
      '0 Sair \n')
   return opçoes



def mostrar_marcas():
   #ler jason, converte json para dicionário
   arquivo = open ('BD_celulares.json') #abre o arquivo
   linhas = arquivo.readline() #le as linhas
   celulares = json.loads(linhas) #converte
   

   os.system('clear')
   marcas = [celulares[0],celulares[7],celulares[15]]
   print('-----------------------------------------------')
   for marca in marcas:
      print(marca['marca'])
   print('-----------------------------------------------\n')
   arquivo.close()


def mostrar_modelos():
   #ler jason, converte json para dicionário
   arquivo = open ('BD_celulares.json') #abre o arquivo
   linhas = arquivo.readline() #le as linhas
   celulares = json.loads(linhas) #converte
   os.system('clear')
   print('-----------------------------------------------')
   for celular in celulares:
      print(celular['modelo'])
   print('-----------------------------------------------')
   print('Role a barra para ver todos modelos')
   print('-----------------------------------------------')

   arquivo.close()


posicoes_modelo = []
def buscar_celular_modelo(nome_buscado):
   posicoes_modelo.clear()

   #ler jason, converte json para dicionário
   arquivo = open ('BD_celulares.json') #abre o arquivo
   linhas = arquivo.readline() #le as linhas
   celulares = json.loads(linhas) #converte

   os.system('clear')
   print('-----------------------------------------------')
   for i in range(len(celulares)):
      if nome_buscado in celulares[i]['modelo']:
         posicoes_modelo.append(str(i))
         print(celulares[i])
   print('-----------------------------------------------')

   arquivo.close()


posicoes_marca = []

def buscar_celular_marca(nome_buscado):
   posicoes_marca.clear()

   #ler jason, converte json para dicionário
   arquivo = open ('BD_celulares.json') #abre o arquivo
   linhas = arquivo.readline() #le as linhas
   celulares = json.loads(linhas) #converte
   
   #posicoes_marca = []
   os.system('clear')
   print('-----------------------------------------------')
   for i in range(len(celulares)):
      if nome_buscado in celulares[i]['marca']:
         posicoes_marca.append(str(i))
         print(celulares[i])
   print('-----------------------------------------------')

   arquivo.close()












posicao_do_cel_escolhido = ''

def entrada_editar(posicoes_marca,posicoes_modelo,posicao_do_cel_escolhido):
   opcoes_de_escolha = ''

   if len(posicoes_marca) >= 1:
      for i in range(len(posicoes_marca)):
         opcoes_de_escolha += str(i)+','
      escolha_resultado = int(input(f'Qual resultado quer selecionar  {opcoes_de_escolha} ? '
         '\nos nº são referentes ao resultado da busca): '))
      posicao_do_cel_escolhido = posicoes_marca[escolha_resultado]

   elif len(posicoes_modelo) >= 1:
      for i in range(len(posicoes_modelo)):
         opcoes_de_escolha += str(i)+','
      escolha_resultado = int(input(f'Qual resultado quer selecionar  {opcoes_de_escolha} ? '
         '\n(os nº são referentes ao resultado da busca): '))
      posicao_do_cel_escolhido = posicoes_modelo[escolha_resultado]
   


def entrada_editar_marca(posicoes_marca,posicao_do_cel_escolhido):
   opcoes_de_escolha = ''


   for i in range(len(posicoes_marca)):
      opcoes_de_escolha += str(i)+','
   escolha_resultado = int(input(f'Qual resultado quer selecion{opcoes_de_escolha} ? '
      '\nos nº são referentes ao resultado da busca): '))
   posicao_do_cel_escolhido = posicoes_marca[escolha_resultado]


def entrada_editar_modelo(posicoes_modelo, posicao_do_cel_escolhido):
   opcoes_de_escolha = ''

   for i in range(len(posicoes_modelo)):
      opcoes_de_escolha += str(i)+','
   escolha_resultado = int(input(f'Qual resultado quer selecionar {opcoes_de_escolha} ? '
      '\n(os nº são referentes ao resultado da busca): '))
   posicao_do_cel_escolhido = posicoes_modelo[escolha_resultado]
   


   
def editar_celular(posicao_do_cel_escolhido):
   print('\nremover, editar ou duplicar registro')
   escolha_editar = input('O que deseja fazer com o celular escolhido?' 
      '\n 1 remover\n 2 editar\n 3 duplicar registro\n')

   arquivo = open ('BD_celulares.json') #abre o arquivo
   linhas = arquivo.readlines() #le as linhas
   celulares = json.loads(linhas) #converte
   
   if escolha_editar > 0:
      for celular in celulares:
         print(celular)

   arquivo.close()


main()

