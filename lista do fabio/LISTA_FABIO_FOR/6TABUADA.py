# Escreva a tabuada dos números de 1 a 10.

contador = 1


def tabuada(contador):
   for numero in range(1, 11):
      print(f'{contador} X {numero} = {contador * numero}')

   if contador < 10:
      contador += 1
      tabuada(contador)


tabuada(contador)
