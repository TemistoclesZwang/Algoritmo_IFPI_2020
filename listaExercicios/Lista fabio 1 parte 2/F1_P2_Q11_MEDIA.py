# 11. Leia 3 números, calcule e escreva a média dos números.

# ENTRADA
n1 = int(input('Insira o 1º número : '))
n2 = int(input('Insira o 2º o número : '))
n3 = int(input('Insira o 3º o número : '))

# PROCESSAMENTO
soma = n1+n2+n3
divisao = soma / 3

# SAIDA
print(f'A média do número digitado é: {divisao}')
