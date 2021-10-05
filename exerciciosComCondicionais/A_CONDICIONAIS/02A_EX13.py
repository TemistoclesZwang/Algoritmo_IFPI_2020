#13. Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são
#diferentes.

def main():
    n1 = int(input('Digite o número 1: '))
    n2 = int(input('Digite o número 2: '))
    n3 = int(input('Digite o número 3: '))
    n4 = int(input('Digite o número 4: '))
    n5 = int(input('Digite o número 5: '))

    maior(n1, n2, n3,n4,n5)



def maior(n1, n2, n3,n4,n5):
    lista = [n1,n2,n3,n4,n5]
    
    print('\nO número maior:')
    print(max(lista))

    print('\nO número menor:')
    print(min(lista))



main()