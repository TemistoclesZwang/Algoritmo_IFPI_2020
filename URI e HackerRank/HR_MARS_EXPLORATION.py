def pricipal():
   s = input('')
   tratar_input(s)

   contador = 0

   for letra in s:
      if letra != 'S' and letra != 'O':
         contador += 1

   print(contador)

def tratar_input(s):
   for caracter in s:
      codigo = ord(caracter)
      if codigo in range(65, 91):
         pass
      else:
         break


pricipal()


