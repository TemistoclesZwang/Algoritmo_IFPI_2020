# 12. Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. Ex.:
# número = 9534 ; soma = 9+5+3+4 = 21.

# ENTRADA
num = int(input('Digite um número: '))


# PROCESSAMENTO
milhar = (num // 1000)
centena = ((num // 100) % 100) % 10
dezena = (num % 100) // 10
unidade = ((num % 100) % 10)


soma = (milhar + centena + dezena + unidade)

# SAIDA
print(
    f'Os elementos digitados foram: {milhar}, {centena}, {dezena}, {unidade}')
print(f'A soma dos elementos digitados é: {soma}')
