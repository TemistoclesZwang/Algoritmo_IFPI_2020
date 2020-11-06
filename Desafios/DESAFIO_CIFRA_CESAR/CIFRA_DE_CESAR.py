def main(texto, chave):

   for letra in texto:
      achar_codigo = ord(letra)

      if achar_codigo in range(97, 123):
         minuscula(texto, achar_codigo, chave)

      elif achar_codigo in range(65, 91):
         maiuscula(texto, achar_codigo, chave)

      else:
         pass


# Verifica se é uma letra minúscula de AaZ (97,123) e rotaciona
def minuscula(texto, achar_codigo, chave):

   rotacionar = achar_codigo + chave

   if rotacionar > 123:
      voltar_começo = 96 + chave  # Se chegar na letra Z retorna para o começa do alfabeto
      novo_caracter = chr(voltar_começo)
      print(novo_caracter)

   else:
      novo_caracter = chr(rotacionar)
      print(novo_caracter)


# Verifica se é uma letra maiúscula de AaZ (65,91) e rotaciona
def maiuscula(texto, achar_codigo, chave):

   rotacionar = achar_codigo + chave
   if rotacionar > 91:
      voltar_começo = 64 + chave  # Se chegar na letra Z retorna para o começa do alfabeto
      novo_caracter = chr(voltar_começo)
      print(novo_caracter)

   else:
      novo_caracter = chr(rotacionar)
      print(novo_caracter)


main('cheer', 7)


