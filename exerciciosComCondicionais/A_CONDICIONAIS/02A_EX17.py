#17. Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
#escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
#são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; 
# 
# 
# se for igual a 4
#divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
#escreva o quadrado dos números lidos.

def main():
    n1 = int(input('Insira o valor 1: '))
    n2 = int(input('Insira o valor 2: '))

    resto_div(n1,n2)
    par_impar(n1,n2)
    multiplique(n1,n2)
    quadrado(n1,n2)

    print('Se nenhum resultado apareceu. Digite outros números. Exemplo: 2 e 4.')


def resto_div(n1,n2):
    resto = n1 % n2
    if resto  == 1:
        soma = n1 + n2
        print (f'O resto da divisão é {resto} sua soma é {soma}')


def par_impar(n1,n2):
    resto = n1 % n2

    if resto  == 2:
        if int(n1) % 2 == 0:
            print (f'{n1} É par')
        else:
            print (f'{n1} É impar')


        if int(n2) % 2 == 0:
            print (f'{n2} É par')
        else:
            print (f'{n2} É impar')
    

def multiplique(n1,n2):
    resto = n1 % n2

    if resto  == 3:
        mult = (n1+n2) * n1
        print (f'A multiplicação é {mult}')


def quadrado(n1,n2):
    resto = n1 % n2

    if resto  == 4:
        if n2 != 0:
            dividir = (n1 + n2) / n2
            print(f'A divisão é {dividir}')

        else:
            print (f'O quadrado do primeiro número é: {n1 ** 2}')
            print (f'O quadrado do segundo número é: {n2 ** 2}')


main()