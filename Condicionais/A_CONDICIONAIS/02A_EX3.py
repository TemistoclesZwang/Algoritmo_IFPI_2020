#3. Leia 3 (três) números, verifique e escreva o maior entre os números lidos.

def main():
    n1 = input('Digite o número 1: ')
    n2 = input('Digite o número 2: ')
    n3 = input('Digite o número 3: ')

    verificar (n1,n2,n3)

def verificar (n1,n2,n3,):
    if n1 > n2 and n1 > n3:
        print (f' {n1} É o maior')

    elif n2 > n1 and n2 >n3:
        print (f' {n2} É o maior')

    elif n3 > n1 and n3 > n2:
        print (f' {n3} É o maior')

    else:
        print ('São iguais')

main()
