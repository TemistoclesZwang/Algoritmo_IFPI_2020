#7. Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele
#corresponde.

#ENTRADA
valor = int(input('Insira o número de minutos: '))

#PROCESSAMENTO
hora = int(valor / 60)
minuto = valor % 60
dia = int(hora / 24)

#SAIDA
print (f'{hora} hora(s) {minuto} minuto(s) {dia} dia(s)')