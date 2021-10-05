# 16 Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:



# ENTRADA
A = int(input('Insira o 1º número: '))
B = int(input('Insira o 2º número: '))
C = int(input('Insira o 3º número: '))


# PROCESSAMENTO
R = (A + B) ** 2
S = (B + C) ** 2
D = (R + S) / 2

# SAIDA
print (f'O resultado da expressão é: {D}')