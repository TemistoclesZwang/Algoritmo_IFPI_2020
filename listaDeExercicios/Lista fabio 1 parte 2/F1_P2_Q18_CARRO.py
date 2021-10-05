# 18 O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor
# e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28%
# e os impostos de 45%, escreva um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

# ENTRADA
custo_fab = int(input('Qual o custo de fábrica ?: '))
# PROCESSAMENTO

distribuidor = (custo_fab / 100) * 28
impostos = (custo_fab / 100) * 45
custo = custo_fab + distribuidor + impostos

# SAIDA
print(f'Custo para o consumidor {custo}')
