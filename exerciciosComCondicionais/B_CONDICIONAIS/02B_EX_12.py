#unidades12.Leiaum número e escrevaseo número é inteiro ou decimal.

def main():
    num = float(input('Digite um numéro: '))
    int_dec(num)


def int_dec(num):
    if(num // 1 == num): 
        print('inteiro')
    else:
        print('Decimal')


main()