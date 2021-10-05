def main():
   quantidade = int(input('Quantos números quer digitar ?: '))
   lista = [-1]*quantidade


   numeros_escolhidos(quantidade,lista)
   par_impar(lista)
   positivo_negativo(lista)
   nova_lista = dobro_e_metade(lista)

   chamar_novos_valores(nova_lista)
   media_valores(nova_lista)


def numeros_escolhidos(quantidade,lista):
   for n in range(quantidade):
      lista[n] = int(input(f'Digite um número para o slot {n}: '))


def par_impar(lista):
   numeros_pares = 0
   numeros_impares = 0

   for numero in lista:
      if numero % 2 == 0:
         numeros_pares += 1
      else:
         numeros_impares += 1
   print (f'Temos {numeros_pares} números pares')
   print (f'Temos {numeros_impares} números ímpares')


def positivo_negativo(lista):
   negativos = 0
   positivos = 0

   for numero in lista:
      if numero < 0:
         negativos += 1
      elif numero >= 0:
         positivos += 1

   print (f'Temos {positivos} números positivos')
   print (f'Temos {negativos} números negativos')


def dobro_e_metade(lista):
   for indice in range (len(lista)):
      if lista[indice] < 0:
         lista[indice] = lista[indice] / 2

      elif lista[indice] >= 0:
         lista[indice] = lista[indice] * 2
   print(f'Números dobrados e divididos pela metade: {lista}')
   return lista

def chamar_novos_valores(nova_lista):
   par_impar(nova_lista)
   positivo_negativo(nova_lista)

def media_valores(nova_lista):
   somar_lista = 0

   for n in nova_lista:
      somar_lista += n

   print(f'A média dos novos valores é: {somar_lista / len(nova_lista)}')


main()