# 1. Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.

def main():
    n1 = input('Digite o número 1: ')
    n2 = input('Digite o número 2: ')
    n3 = input('Digite o número 3: ')
    
    verificar (n1,n2,n3)

def verificar (n1,n2,n3):
    if n1 == n2 and n2 == n3 and n1 == n3:
        print('Tem três números iguais')

    elif n1 == n2 or n2 == n3 or n1 == n3:
        print('Tem dois iguais')
        
    else:
        print('Não tem iguais')

main()