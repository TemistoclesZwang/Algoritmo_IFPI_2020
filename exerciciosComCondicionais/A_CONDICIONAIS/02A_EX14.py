#14. Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.


def main():
    n1 = int(input('Insira o número 1: '))
    n2 = int(input('Insira o número 2: '))
    n3 = int(input('Insira o número 3: '))
    n4 = int(input('Insira o número 4: '))
    n5 = int(input('Insira o número 5: '))

    media(n1,n2,n3,n4,n5)


def media(n1,n2,n3,n4,n5):
    calc_media = (n1 + n2 + n3 + n4 + n5) / 5
    print (f'A média é {calc_media}')

    if n1 > calc_media:
        print (f'Esse número é maior que a média: {n1}')

    elif n2 > calc_media:
        print (f'Esse número é maior que a média: {n2}')

    elif n3 > calc_media:
        print (f'Esse número é maior que a média: {n3}')

    elif n4 > calc_media:
        print (f'Esse número é maior que a média: {n4}')
     
    elif n5 > calc_media:
        print (f'Esse número é maior que a média: {n5}')
    

main()