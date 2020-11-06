def main():
   s = input('')
   contador = 1
   achar_codigo(s,contador)


def achar_codigo(s,contador):
   for letra in s:
      codigo = ord(letra)

      if codigo in range(65,91):
         contador += 1
   print(contador)

main()
