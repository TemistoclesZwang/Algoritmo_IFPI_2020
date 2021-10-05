# 9. Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.

# ENTRADA
num = int(input('Insira um número de 3 dígitos: '))

# PROCESSAMENTO

resto = (num % 100)
num1 = str(num // 100)
num2 = str(resto // 10)
num3 = str(resto % 10)
inverso = int(num3 + num2 + num1)
diferença = num - inverso

# SAIDA
print(f'A diferença de seu número com o inverso é: {diferença}')
