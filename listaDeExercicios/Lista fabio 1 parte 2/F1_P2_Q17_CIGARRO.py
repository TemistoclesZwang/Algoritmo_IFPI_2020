#17 Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: 
# o número de anos que ele fuma, o no de cigarros fumados por dia 
# e o preço de uma carteira (1 carteira tem 20 cigarros).

#ENTRADA
anos_fuma = int(input('Quantos anos você fuma?: '))
cigarros_dia = int(input('Quantos cigarros você fuma por dia?:'))
preço_maço = int(input('Quanto custa seu maço de cigarro ?: '))

#PROCESSAMENTO
dinheiro_dia = (preço_maço / 20) + cigarros_dia
dinheiro_mês = dinheiro_dia * 30
dinheiro_anos = dinheiro_mês * (anos_fuma * 12) 


#SAIDA
print (f' Você fuma {cigarros_dia} cigarros por dia e gasta R$ {dinheiro_mês:.2f} por mês') 
print (f'totalizando R${dinheiro_anos:.2f} em {anos_fuma} anos')
