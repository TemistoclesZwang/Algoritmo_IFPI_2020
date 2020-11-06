# 8. Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva
# sua idade exata (em anos).


def main():
    dia = int(input('Insira o dia de seu nascimento: '))
    mes = int(input('Insira o mês de seu nascimento: '))
    ano = int(input('Insira o ano de seu nascimento: '))

    data_hoje(dia, mes, ano)


def data_hoje(dia, mes, ano):
    from datetime import date

    data_atual = date.today()
    print (f'A data atual é {data_atual}')


    idade = data_atual.year - ano #ano atual menos o ano inserido
    print (f'Sua idade em anos é {idade}')

main()
