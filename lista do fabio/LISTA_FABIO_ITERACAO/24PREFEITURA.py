'''A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e
número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e
escreva:
a) média de salário da população;
b) média de número de filhos;
c) percentual de pessoas com salário de até R$ 1.000,00.'''

import random

class color:
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'

n = int(input('Digite a amostra (quantidade de pessoas): '))

contador = 0
soma_salarios = 0
soma_filhos = 0
pessoas_até_mil = 0

while contador <= n - 1:

   # gerador de codigo,horas, e dependetes
   id_cidadao = random.randint(1000000, 10000000)
   salario = random.randint(500, 2990)
   numero_filhos = random.randint(0, 5)

   #somando os dados
   soma_salarios = soma_salarios + salario
   soma_filhos = soma_filhos + numero_filhos

   media_salarios = soma_salarios / n
   media_filhos = soma_filhos / n

   contador += 1
   if salario <= 1000:
      pessoas_até_mil += 1
   else:
      pass
   print(f'Identidade do cidadão: {id_cidadao}')
   print(f'Salário: {salario}')
   print(f'Número de filhos: {numero_filhos}\n')


#porcentagem
porcentagem = (pessoas_até_mil * n) / 100


print(f'{color.HEADER}Média salarial: {color.OKGREEN}{media_salarios}{color.ENDC}')
print(f'{color.HEADER}Média filhos: {color.FAIL}{media_filhos}{color.ENDC}')
print(f'{color.HEADER}Porcentagem de pessoas que recebem até R$ 1.000,00: {color.FAIL}{porcentagem}%{color.ENDC}')