arquivo = open(
   '/home/temistocles/Documentos/IFPI/IFPI_ALG_2020/atividades PENSE PYTHON/words.txt')



def main():
   print(
      '1 palavras com mais de 20 letras \n'
      '2 palavras sem o "e" \n'
      '3 letras probidas \n'
      '4 letras não proibidas \n'
      '5 todas as letras \n'
      '6 abecedario \n')
      
   entrada = int(input('Escolha uma opção:'))

   if entrada == 1 :
      mais_de_20(arquivo)

   elif entrada == 2 :
      has_no_e(arquivo)

   elif entrada == 3 :
      avoids()

   elif entrada == 4 :
      uses_only()

   elif entrada == 5 :
      uses_all()

   elif entrada == 6 :
      is_abecedarian()


def mais_de_20(arquivo):
   for linha in arquivo:
      palavra = linha.strip()
      
      if len(palavra) > 20:
         print(palavra)
         

   arquivo.close()


def has_no_e(arquivo):
   total_palavras = 0
   palavras_sem_e = 0

   for linha in arquivo:
      palavra = linha.strip()
      total_palavras += 1

      if 'e' not in palavra:
         print(f'{palavra} True')
         palavras_sem_e += 1
   print('\n')

   porcentagem = (palavras_sem_e / total_palavras) * 100
   print(f'Porcentagem de palavras com "e": {porcentagem:.0f}%')

   arquivo.close()


def avoids():
   palavra = input('Insira sua palavra: ')
   letras_proibidas = input('Digite as letras proibidas(juntas,sem espaço): ').split()

   for letra in palavra:
      if letra not in letras_proibidas:
         print( True)
      else:
         print( False)


def avoids_pt2(arquivo):
   letras_proibidas = input('Digite as letras proibidas: ')
   lista_compara = []
   contagem_sem_probidas = []

   for letra_proi in letras_proibidas:  # para cada letra da lista de probidas
      for linha in arquivo:  # para cada,palavra, linha do arquivo de texto
         linha = linha.strip() #retirar o \n
         lista_compara = list(linha) # A lista recebe cada letra da palavra que está no arquivo de txt
         for letra in lista_compara:
            if letra != letra_proi and linha not in contagem_sem_probidas: 
               #se a letra da palavra do arquivo de texto for diferente das letras probidas
               #E se aquela palavra da respectiva letra não estivar ainda na lista, adcione-a
               contagem_sem_probidas.append(linha)
   arquivo.close()
   print(contagem_sem_probidas)


def uses_only():
   palavra = input('Digite sua palavra: ')
   letras_achar = input('Digite suas letras: ')
   for letra in palavra:
      if letra not in letras_achar:
         return False
      else:
         return True


def uses_all():
   palavra = input('Digite sua palavra: ').upper()
   letras_achar = input('Digite suas letras(sem espaço): ').upper()

   if letras_achar in palavra:
      return True
   return False


def is_abecedarian():
   palavra = input('Insira uma palavra: ')

   if len(palavra) <= 1:
      return True 
   if palavra[0] > palavra[1]:
      return False
   return palavra[1:]


main()