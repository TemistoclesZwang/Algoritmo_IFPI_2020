#12. Leia 1 (um) número inteiro e escreva se este número é par ou impar.

def main():
    numero = int(input('Insira um número: '))
    verificar(numero)
   

def verificar(numero):
    if int(numero) % 2 == 0:
        print ('É par')
    else:
        print ('É impar')

main()


