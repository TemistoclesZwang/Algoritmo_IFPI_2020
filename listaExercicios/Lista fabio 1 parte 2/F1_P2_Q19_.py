# 19 Escreva um algoritmo que, tendo como dados de entrada 2
# pontos quaisquer no plano, ponto1 (x1,y1) e ponto2 (x2,y2),
# escreva a distância entre eles, conforme fórmula abaixo.

p1y = int(input('Digite o ponto 1 de y: '))
p1x = int(input('Digite o ponto 1 de x: '))

p2y = int(input('Digite o ponto 2 de y: '))
p2x = int(input('Digite o ponto 2 de x: '))


calc1 = (p2x - p1x) ** 2
calc2 = (p2y + p1y) ** 2
soma = calc1 + calc2
raiz = soma ** (1 / 2)

print(soma)
print(raiz)
