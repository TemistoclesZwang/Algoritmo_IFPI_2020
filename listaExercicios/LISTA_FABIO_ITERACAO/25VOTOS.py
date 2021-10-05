'''Em uma eleição presidencial existem 3 (três) candidatos. Os votos são informados através de códigos.

Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:

· 1, 2, 3 = voto para os respectivos candidatos;
· 9 = voto nulo;
· 0 = voto em branco;

Escreva um algoritmo que leia o código votado por N eleitores. Ao final, calcule e escreva:
a) total de votos para cada candidato;
b) total de votos nulos;
c) total de votos em branco;
d) quem venceu a eleição.'''
import random

n = int(input('Número de eleitores: '))
contador = 0

# teclas
candidato1 = 0
candidato2 = 0
candidato3 = 0
voto_branco9 = 0
voto_nulo0 = 0

while contador < n:
   voto = random.randint(1, 5)

   if voto == 1:
      candidato1 = candidato1 + 1

   elif voto == 2:
      candidato2 = candidato2 + 1

   elif voto == 3:
      candidato3 = candidato3 + 1

   elif voto == 4:
      voto_branco9 = voto_branco9 + 1

   elif voto == 5:
      voto_nulo0 = voto_nulo0 + 1

   contador += 1

vencedor = 0

if candidato1 > candidato2 and candidato1 > candidato3:
   vencedor = 'candidato1'

if candidato2 > candidato1 and candidato2 > candidato3:
   vencedor = 'candidato2'

if candidato3 > candidato1 and candidato3 > candidato2:
   vencedor = 'candidato3'

else:
   print('Empate, aguarde pelo segundo turno.')

print(
   f'Total de votos para cada candidato - candidato1: {candidato1},candidato2: {candidato2},candidato3: {candidato3}')
print(f'Total de votos nulos: {voto_nulo0}')
print(f'Total devotos em branco: {voto_branco9}')
print(f'Vencedor: {vencedor}')
