def main():
   tamanho = int(input(''))
   senha = input('')
   
   lista_verificados = []

   numbers = "0123456789"
   lower_case = "abcdefghijklmnopqrstuvwxyz"
   upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   especiais = "!@#$%^&*()-+"

   verificar_tamanho(tamanho,lista_verificados)
   verificar(especiais,lista_verificados,senha)
   verificar(numbers,lista_verificados,senha)
   verificar(lower_case,lista_verificados,senha)
   verificar(upper_case,lista_verificados,senha)

   analisar_senha(lista_verificados)


def verificar_tamanho(tamanho,lista_verificados):
   if tamanho >= 6:
      lista_verificados.append(tamanho)


def verificar(criterio,lista_verificados,senha):
   for letra in criterio:
      if letra in senha:
         lista_verificados.append(criterio)
         break

def analisar_senha(lista_verificados):
   quantidade_itens = len(lista_verificados)

   if quantidade_itens < 6:
      falta = 6 - quantidade_itens
      print(falta)


main()

