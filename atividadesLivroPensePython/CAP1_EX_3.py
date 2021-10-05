# Se você correr 10 quilômetros em 42 minutos e 42 segundos,
# qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?

'''Passo médio'''
# Entrada
milha = 0.62
dez_milhas = milha * 10

# Processamento
media_min = int(42 / dez_milhas)
media_segundos = 42 + 7

# Saída
print(f'Seu passo médio é: {media_min} minutos {media_segundos} segundos por milha')

'''Velocidade'''
# Processamento
hora = int(60 / 6)
segundos = int(122 / 60)

# Saída
print(f'Sua velocidade média é: {hora+segundos} milhas por hora.')
