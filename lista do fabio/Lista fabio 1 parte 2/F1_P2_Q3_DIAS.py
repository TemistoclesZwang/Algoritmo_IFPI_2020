# ENTRADA
dias = int(input('Insira o número de dias: '))
# PROCESSAMENTO

semana = int(dias / 7)
resto = dias % 7

# SAIDA
print(f'{dias} Dias são {semana} semana(s) e {resto} dia(s)')
