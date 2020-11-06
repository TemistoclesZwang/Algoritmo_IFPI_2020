'''Uma determinada empresa armazena para cada funcionário uma ficha contendo o código, o número de
horas trabalhadas e o seu no de dependentes. Considerando que a empresa paga R$ 12,00 por hora e R$
40,00 por dependentes e que sobre o salário são feitos descontos de 8,5% para o INSS e 5% para IR.

Escreva um algoritmo que leia o código, número de horas trabalhadas e número de dependentes de N
funcionários. Após a leitura de cada ficha, escreva os valores descontados para cada imposto e o salário
líquido do funcionário.'''
import random


class bcolors:
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'

contador = 0
codigo = 0
horas_trabalhadas = 0
dependentes = 0

# características da empresa
funcionarios = 10
por_hora = 12
por_dependente = 40
inss = 8.5
ir = 5

while contador < funcionarios:

   # gerador de codigo,horas, e dependetes
   random_codigo = random.randint(100000, 1000000)
   random_horas_trabalhadas = random.randint(150, 275)
   random_dependentes = random.randint(0, 5)

   #Gerador de nomes
   lista_nomes = ['Javascript do React Ferreira','Amim Amou Amado','Lança Perfume Rodometálico de Andrade','Naída Navinda Navolta Pereira','Espere Em Deus Matheus','Safira Azul Esverdeada','Bandeirante do Brasil Paulistano','Céu Azul do Sol Poente','Felicidade do Lar Brasileiro','Afília Demaria de Nazaré','Maiquel Edy Marfy','Antônio Moura Pacífico de Oliveira Sossegado']

   selecionar_nome = lista_nomes[contador]

   # calculos
   horas_trabalhadas = random_horas_trabalhadas * por_hora
   dependentes = random_dependentes * por_dependente

   salario_bruto = horas_trabalhadas + dependentes

   desconto_inss_ir = (ir + inss * salario_bruto) / 100


   salario_liquido = salario_bruto - (desconto_inss_ir)

   contador += 1

   # mostrar dados
   print('\n')
   print(f'Nome do funcionário: {bcolors.OKGREEN}{ selecionar_nome}{bcolors.ENDC}')
   print(f'Codigo do funcionario: {random_codigo}')
   print(f'Horas trabalhadas: {random_horas_trabalhadas}h')
   print(f'Número de dependetes: {random_dependentes}')
   print(f'   Salário bruto: R$ {bcolors.HEADER}{salario_bruto :.2f}{bcolors.ENDC}')
   print(f'   Salário líquido: R$ {bcolors.OKBLUE}{salario_liquido :.2f}{bcolors.ENDC}')


