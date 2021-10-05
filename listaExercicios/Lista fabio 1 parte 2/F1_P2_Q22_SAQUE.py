# 22Um algoritmo para gerenciar os saques de um caixa eletrônico deve possuir
# algum mecanismo para decidir o numero de notas de cada valor que deve ser
# disponibilizado para o cliente que realizou o saque. Um possível critério
# seria o da "distribuição ótima" no sentido de que as notas de menor valor
# disponíveis fossem distribuídas em número mínimo possível. Por exemplo,
# se a maquina só dispõe de notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1,
# para uma quantia solicitada de R$ 87, o algoritmo deveria indicar
# uma nota de R$ 50, três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1.
# Escreva um algoritmo que receba o valor da quantia solicitada e retorne a distribuição
# das notas de acordo com o critério da distribuição ótima.


# ENTRADA
saque = int(input('Quanto quer sacar?: '))

# PROCESSAMENTO
cem = saque // 100
resto = saque % 100

cinquenta = resto // 50
resto = resto % 50

vinte = resto // 20
resto = resto % 20

dez = resto // 10
resto = resto % 10

cinco = resto // 5
resto = resto % 5

dois = resto // 2

# SAIDA

resultado = "Aguarde..."
resultado = resultado + f'\n {cem} x R$ 100'
resultado = resultado + f'\n {cinquenta} x R$ 50'
resultado = resultado + f'\n {vinte} x R$ 20'
resultado = resultado + f'\n {dez} x R$ 10'
resultado = resultado + f'\n {cinco} x R$ 5'
resultado = resultado + f'\n {dois} x R$ 2'

print(resultado)