# 10. Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.

def main():
    dia = int(input('Insira o dia: '))
    mes = int(input('Insira o mês: '))
    ano = int(input('Insira o ano: '))

    verificar(dia,mes,ano)


def verificar(dia,mes,ano):
    if dia > 30:
        print('Erro.O mês vai de 1 até 30.')

    elif mes > 12:
        print('Erro. Os meses vão de 1 até 12.')

    elif ano // 1000 == 0:
        print('Erro. Os anos precisam ter 4 dígitos.')

    else:
        print('Sua data é válida!')


main()