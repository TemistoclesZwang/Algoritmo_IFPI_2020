
def main():

   # opcoes()


   # lista_coligacoes()
   # lista_candidatos()
   total_votos_validos()
   # quociente_e()
   # lista_coligacoes()
   # filtrar_votos_por_coligacao()
   # quociente_p()
   # teste()

def opcoes():
   print('1 xxxxx: \n'
      '2 xxxxx: \n'
      '3 xxxxx: \n'
      '4 xxxxx: \n')


   return input('O que deseja fazer?')


#letra A
def lista_coligacoes():
   arquivo = open('/home/themiszwang/Documentos/IFPI/IFPI_ALG_2020/DESAFIO_ELEICOES/partidos_coligacoes.csv', 'r').readlines()
   partidos_coligacoes = []

   for linha in arquivo:
      linha = linha.split(';') 
      dic = {'coligação': linha[0].rstrip('\n'),'total_votos': 0, 'qtd_vagas(QE)': 0, 'votos_sobra': 0} 
      partidos_coligacoes.append(dic)
   for l in partidos_coligacoes:
      print(l)


   return partidos_coligacoes


#letra B
def lista_candidatos():
   arquivo = open('/home/themiszwang/Documentos/IFPI/IFPI_ALG_2020/DESAFIO_ELEICOES/votos_cadidatos.csv', 'r').readlines()
   candidatos = []

   for linha in arquivo:
      linha = linha.split(';') #quebra onde tiver ;
      # dic ['nome'] = linha[0]
      dic = {'nome': linha[0],'numero': linha[1], 'nome_partido': linha[2], 'coligação': linha [3], 'total_votos': linha[4].rstrip('\n')} #linha 0,1,2,3,4 nome,numero etc que está naquela linha e faz isso em todas
      candidatos.append(dic)

   return candidatos
      
      
#letra C
def total_votos_validos():
   candidatos= lista_candidatos()
   soma_votos = 0
   for candidato in candidatos:
      soma_votos += int(candidato['total_votos'])
   print(soma_votos)
   
   return soma_votos


#letra D
def quociente_e():
   #verificar se o QE é calculado para cada partido
   soma = total_votos_validos()
   QE = soma // 29 #29vagas
   # print(QE)

   return QE


#letra E
def filtrar_votos_por_coligacao():
   #verifica cada coligação da lista coligação
   #verifica cada chave 'coligação' da lista candidatos
   #se as duas forem iguais, pega os votos e soma daquela coligação apenas

   cadidatos = lista_candidatos()
   coligacoes = lista_coligacoes ()

   coligacoes_e_votos = []
   soma = 0

   for coligacao in coligacoes:
      for candidato in cadidatos:
         if coligacao['coligação'] == candidato['coligação']:
            soma += int(candidato['total_votos'])
      dic = {'coligação': coligacao['coligação'], 'total_votos': soma}
      coligacoes_e_votos.append(dic)

   # for i in coligacoes_e_votos:
   #    print(i)
   return coligacoes_e_votos


#letra F
def quociente_p():
   coligacoes_e_votos = filtrar_votos_por_coligacao()
   qe = quociente_e()
   QP = []

   for partido in coligacoes_e_votos:
      calculo_qp = partido['total_votos'] // qe
      dic = {'coligação': partido['coligação'] ,'qtd_vagas_QP': calculo_qp}
      QP.append(dic)

   for i in QP:
      print(i)

   return QP







main()

