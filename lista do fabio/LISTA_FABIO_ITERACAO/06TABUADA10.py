contador = 1
n = 1

def tabuada(contador,n):   
   while contador <= 10:
      calc = contador * n
      print(f'\033[94m{n}\033[0m X \033[91m{contador}\033[0m = \033[95m{calc}\033[0m \n') 
      contador += 1
   print('\033[92m -------------------------------------- \033[0m' )
   prin)t('\n'

   if contador > 10 and n < 10:
      contador = 1
      n += 1
      tabuada(contador,n)

tabuada(contador,n)

# Escreva a tabuada dos números de 1 a 10.