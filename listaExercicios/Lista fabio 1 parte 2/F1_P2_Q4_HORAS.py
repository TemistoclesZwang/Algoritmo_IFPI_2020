# 4. Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.

# ENTRADA
segundos = int(input('Insira os segundos: '))
# PROCESSAMENTO

horas = int(segundos / 60)
minutos = segundos % 60

# SAIDA
print(f'{segundos}segundos São {horas} horas e {minutos} minutos')
