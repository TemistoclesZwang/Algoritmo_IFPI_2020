# 10. Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso.
# (Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).

# ENTRADA
num = int(input('Insira um número de 3 dígitos: '))

# PROCESSAMENTO

num1 = ((num // 100) % 100) % 10 #Unidade
num2 = (num % 100) // 10 # Dezena
num3 = ((num % 100) % 10) #Centena

calc1 = num3 + num1
calc2 = num2 + num2
calc3 = num1 + num3

# SAIDA
print(f'A soma de seu número com o inverso é: {calc1}{calc2}{calc3}')
