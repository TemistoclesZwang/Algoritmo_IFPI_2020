lista_para_inverter = []
lista_invertidos = []
lista_truncada = []
lista_final = []

def main():
   chave = 3
   numero_linhas = int(input('Digite o número de linhas: '))
   for numero in range(1, numero_linhas + 1):
      texto = input(f'linha: {numero} Digite os caractéres: ')
#passo 1
      rotacionar_maimin(texto, chave)
   imprimir_fim(lista_final)


# Essa função faz a rotação das maiúsculas e minúsculas
def rotacionar_maimin(texto, chave):
   for letra in texto:
      achar_codigo = ord(letra)

      # Verifica se é uma letra minúscula de AaZ (97,123)
      if achar_codigo in range(97, 123):
         achar_letra(texto, achar_codigo, chave)

      # Verifica se é uma letra maiúscula de AaZ (65,91)
      elif achar_codigo in range(65, 91):
         achar_letra(texto, achar_codigo, chave)
      else:
         lista_para_inverter.append(letra)
#passo 2
   inverter_carac()  
#passo 3
   lista_final.append(lista_invertidos + lista_truncada)
   limpar_listas(lista_invertidos, lista_truncada, lista_para_inverter)


def achar_letra(texto, achar_codigo, chave):
   rotacionar = achar_codigo + chave
   caracter = chr(rotacionar)
   lista_para_inverter.append(caracter)
   # print(caracter)


def inverter_carac(): 
   invertido = lista_para_inverter[::-1]
   tamanho = len(invertido)
   calc = (tamanho // 2)

   for caracter in range(0, calc): #Adciona os caracteres invertidos em uma nova lista
      lista_invertidos.append(invertido[caracter])
   metade_truncada(invertido,calc)


def metade_truncada(invertido,calc):
   metade = invertido[calc:]
   for caracter in metade:  # Deslocar uma casa para a esquerda
      codigo_caracter = ord(caracter)
      deslocar_esquerda = codigo_caracter - 1
      letra_deslocada = chr(deslocar_esquerda)
      lista_truncada.append(letra_deslocada)


def limpar_listas(lista_invertidos, lista_truncada, lista_para_inverter):
   lista_para_inverter.clear()
   lista_invertidos.clear()
   lista_truncada.clear()


def imprimir_fim(lista_final):
   for conjunto in lista_final:
         for letra in conjunto:
            print(f'{letra}', end='')
         print('')


main()