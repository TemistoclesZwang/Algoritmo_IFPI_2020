# 14. Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

# ENTRADA
dias = int(input('Quantos dias de vida você tem?: '))

# PROCESSAMENTO
meses = int(dias / 365)
anos = int(meses / 12)

# SAIDA
print(f'Você tem {dias} dias. Que equivalem a {meses} meses e {anos} anos.')
