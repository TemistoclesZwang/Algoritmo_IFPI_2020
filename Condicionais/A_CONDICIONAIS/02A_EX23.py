#23. Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais recente.


def main():
    dia1 = int(input('Insira o dia 1: '))
    mes1 = int(input('Insira o mês 1: '))
    ano1 = int(input('Insira o ano 1: '))

    dia2 = int(input('Insira o dia 2: '))
    mes2 = int(input('Insira o mês 2: '))
    ano2 = int(input('Insira o ano 2: '))

    verificar(dia1,mes1,ano1,dia2,mes2,ano2)


def verificar(dia1,mes1,ano1,dia2,mes2,ano2):
    soma1 = dia1 + mes1 + ano2
    soma2 = dia2 + mes2 + ano2

    if soma1 > soma2:
        print(f'Essa é a data mais recente {dia1}/{mes1}/{ano1}')

    elif soma2 > soma1:
        print(f'Essa é a data mais recente {dia2}/{mes2}/{ano2}')


main()



