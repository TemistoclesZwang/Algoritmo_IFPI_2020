#27. Determine a idade de uma pessoa, em anos, meses e dias, dadas a data (dia, mês e ano) do seu
#nascimento e a data (dia, mês e ano) atual.

def main():
    dia = int(input('Insira o dia de seu nascimento: '))
    mes = int(input('Insira o mês de seu nascimento: '))
    ano = int(input('Insira o ano de seu nascimento: '))
    verifica_num(dia,mes,ano)




def verifica_num(dia,mes,ano):
    if dia > 31 or mes > 12:
        print('\nErro. Os dias vão de 1 até 31')
        print('Erro. Os meses vão de 1 até 12')

    elif dia < 31 or mes < 12:
        idade(dia,mes,ano)

def idade(dia,mes,ano):
    from datetime import date

    data_atual = date.today()
    print (f'\nA data atual é {data_atual}')


    if dia > data_atual.day:
        print(f'\nDias {dia - data_atual.day}')
    elif data_atual.day > dia:
        print(f'\nDias {data_atual.day - dia}')

    if mes > data_atual.month:
        print(f'Meses {mes - data_atual.month}')
    elif data_atual.month > mes:
        print(f'Meses {data_atual.month - mes}')

    if ano > data_atual.year:
        print(f'Anos {ano - data_atual.year}')
    elif data_atual.year > ano:
        print(f'Anos {data_atual.year - ano}')



main()