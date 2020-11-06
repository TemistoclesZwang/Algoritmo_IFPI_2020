# 5. Leia 3 (três) números e escreva-os em ordem crescente.


def main():
    n1 = int(input('Digite o número 1: '))
    n2 = int(input('Digite o número 2: '))
    n3 = int(input('Digite o número 3: '))

    verificar(n1,n2,n3)

def verificar(n1,n2,n3):
    lista = [n1,n2,n3]
    print(sorted(lista))


main()
