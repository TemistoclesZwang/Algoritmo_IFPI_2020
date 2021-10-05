# 13. Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

# ENTRADA
idade = int(input('Quantos anos você tem?: '))
q_meses = int(input('Falta quantos meses para seu aniversário?: '))


# PROCESSAMENTO

meses = (idade  * 12)
dias = q_meses / 30
calc = int(meses + dias) * 365


# SAIDA
print(f'Você tem {idade} anos e {q_meses} meses. Que equivalem a: {calc} dias')
