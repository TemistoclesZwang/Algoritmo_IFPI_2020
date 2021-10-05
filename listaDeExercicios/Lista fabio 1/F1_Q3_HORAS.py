# 3. Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.

# Entrada
minutos = int(input('Insira os minutos:'))

# Processamento
conversao = minutos
horas = int(minutos / 60)
resto = (minutos % 60)

# Saida
print(f'{minutos} minutos é igual a {horas} horas e {resto} minutos')
