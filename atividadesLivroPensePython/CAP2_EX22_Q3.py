'''
Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro),
então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) 
e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?
'''
# Entrada

todos_minutos = 52 + 8 + 21 + 8
todos_segundos = 15 + 36 + 15
hora_saída = 6

# processamento
horas = int(todos_minutos / 60)
minutos = int(todos_minutos) % 60
segundos = 6 % todos_segundos
minutos_r = int((6 / 6) + minutos)

# Saída
print(f'Chegará para o café {horas+hora_saída} horas {minutos_r} minutos {segundos} segundos')
