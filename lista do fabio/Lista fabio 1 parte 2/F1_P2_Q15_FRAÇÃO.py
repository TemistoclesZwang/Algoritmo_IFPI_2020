# 15. Leia 2 (duas) frações (numerador e denominador),
# calcule e escreva a soma destas frações, escrevendo o resultado em forma de fração.

# ENTRADA
n1 = int(input('Digite o numerador 1: '))
d1 = int(input('Digite o denominador 1: '))

n2 = int(input('Digite o numerador 2: '))
d2 = int(input('Digite o denominador 2: '))

# PROCESSAMENTO
calc_d = d1 * d2
calc_n = (calc_d // d1) * n1 + (calc_d // d2) * n2

# SAIDA
print(f'A soma das frações é {calc_n}/{calc_d}')
