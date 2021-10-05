#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# 1.Álcool:·até 20 litros, desconto de 3% por litro·acima de 20 litros, desconto de 5% por litro2.
# Gasolina:·até 20 litros, desconto de 4% por litro·acima de 20 litros, desconto de 6% por litro.
# Escreva  um  algoritmo  que  leia  o  número  de  litros  vendidos,  o  tipo  de  combustível  
# (codificado  da seguinte forma: A-álcool, G-gasolina), calcule e imprimao valor 
# a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

def main():
    tipo = input('Álcool ou Gasolina?: ').upper()
    litros = int(input('Quantos litros vai commprar?: '))
    total(tipo,litros)


def total(tipo,litros):
    if tipo == 'ÁLCOOL' and litros <= 20:
        porcentagem = (3 * litros) / 100
        preço = litros * 1.90
        print(f'\nO valor a pagar é R$ {preço - porcentagem :.2f}')

    elif tipo == 'ÁLCOOL' and litros > 20:
        porcentagem = (5 * litros) / 100
        preço = litros * 1.90
        print(f'\nO valor a pagar é R$ {preço - porcentagem :.2f}')


    if tipo == 'GASOLINA' and litros <=20:
        porcentagem = (4 * litros) / 100
        preço = litros * 1.90
        print(f'\nO valor a pagar é R$ {preço - porcentagem :.2f}')

    elif tipo == 'GASOLINA' and litros > 20:
        porcentagem = (6 * litros) / 100
        preço = litros * 2.50
        print(f'\nO valor a pagar é R$ {preço - porcentagem :.2f}')

main()