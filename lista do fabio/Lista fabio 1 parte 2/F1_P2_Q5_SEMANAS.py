# 5. Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele corresponde.

# ENTRADA
horas = int(input('Insira as horas: '))

# PROCESSAMENTO

semanas = int(horas / 168) #Uma semana tem 168 horas
resto_h = horas % 24
dias = int(horas / 24) % 7

# SAIDA
print(f'{horas} Hora(s) são {semanas} semana(s) e {dias} dia(s) e {resto_h} horas')

