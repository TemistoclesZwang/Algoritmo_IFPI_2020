# 8. Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.

# ENTRADA
num = int(input('Insira um número binário de 4 dígitos: '))

bin0 = (num // 1000)
bin1 = ((num // 100) % 100) % 10
bin2 = (num % 100) // 10
bin3 = ((num % 100) % 10)

# PROCESSAMENTO
n_digitado = bin0, bin1, bin2, bin3

posi0 = 0
posi1 = 1
posi2 = 2
posi3 = 3

re1 = bin0 * 2 ** posi3
re2 = bin1 * 2 ** posi2
re3 = bin2 * 2 ** posi1
re4 = bin3 * 2 ** posi0

soma = re1+re2+re3+re4

# SAIDA
print(f'O número digitado {n_digitado} em base decimal é {soma}')
