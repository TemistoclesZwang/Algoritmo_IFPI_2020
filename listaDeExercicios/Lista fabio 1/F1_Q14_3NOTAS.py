# Entrada
n1 = int(input('Insira a nota 1: '))
n2 = int(input('Insira a nota 2: '))
n3 = int(input('Insira a nota 3: '))

# Processamento
peso_n1 = int(3)
peso_n2 = int(2)
peso_n3 = int(1)
multi = (n1 * peso_n1) + (n2 * peso_n2) + (n3 * peso_n3)
pesos = peso_n1 + peso_n2 + peso_n3

# Saída
print(f'Sua média é {multi / pesos:.2f}')
