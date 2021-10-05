# 6. Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

# ENTRADA
meses = int(input('Insira um número de dias: '))

# PROCESSAMENTO
mes = 30
anos = 365

calc_mes = int(meses / 30)
calc_dia = int(meses % 30)
calc_ano = int(meses / 365)

# SAIDA
print(f'{meses} dias são {calc_mes} meses')
print(f'{calc_dia} dia(s)')
print(f'e {calc_ano} ano(s)')
