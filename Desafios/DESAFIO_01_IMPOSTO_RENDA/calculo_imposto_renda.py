#Usando pensamento computacional e as ferramentas de automação já conhecidas, 
# peça a renda do usuário e em calcule
#  e exiba qual o valor de imposto de renda real ele deverá pagar pela tabela atual sem correção
#  e pela tabela corrigida. Quem tem renda tributável de R$ 13.800,00 - paga quanto? deveria pagar somente quanto? 
#


def main():
    #Instruções
    print('~' * 30)
    print('Seja bem-vindo. Insira o valor de sua renda. Siga as regras de como digitar o valor, \nusando ponto para separar apenas os centavos.')
    print(f'Por exemplo, uma pessoa que ganha R$ 13.800,00 DIGITE 13800.00 \ncom esse salário irá pagar na tabela desatualizada: R$37950.0 \ne 37950 na tabela atualizada.')
    print('~' * 30)
    #entrada
    renda = float(input('Informe sua renda: '))

    #chamada funções
    gerar_tabela_atual(renda)
    print('-' * 30)
    gerar_tabela_corrigida(renda)

def gerar_tabela_atual(renda):

    if renda <= 1903.98:
        print('-' * 30)
        print ('Tabela desatualizada: Alíquota 0')
        print(f'Tabela desatualizada: Valor a pagar: R${0}')


    elif renda <= 2826.65:    
        print('-' * 30)
        porcentagem = (renda * 7.5 ) / 100
        print('Tabela desatualizada: Alíquota 7.5')
        print(f'Tabela desatualizada: Valor a pagar: R${porcentagem}')


    elif renda <= 3751.05:
        print('-' * 30)
        porcentagem = (renda * 15) / 100
        print('Tabela desatualizada: Alíquota 15')   
        print(f'Tabela desatualizada: Valor a pagar: R${porcentagem}')


    elif renda <= 4664.68:
        print('-' * 30)
        porcentagem = (renda * 22.5) / 100
        print('Tabela desatualizada: Alíquota 22,5')
        print(f'Tabela desatualizada: Valor a pagar: R${porcentagem}')


    else:
        print('-' * 30)
        porcentagem = (renda * 27.5) / 100
        print('Tabela desatualizada: Alíquota 27,5')
        print(f'Tabela desatualizada: Valor a pagar: R${porcentagem}')



def gerar_tabela_corrigida(renda):

    if renda <=  3881.65:
        print ('Tabela atualizada: Alíquota 0')
        print(f'Tabela atualizada: Valor a pagar: R${0}')


    elif renda <= 5714.11:

        porcentagem = (renda * 7.5 ) / 100
        print('Tabela atualizada: Alíquota 7.5')
        print(f'Tabela atualizada: Valor a pagar: R${porcentagem}')


    elif renda <= 7654.67:

        porcentagem = (renda * 15) / 100
        print('Tabela atualizada: Alíquota 15%')   
        print(f'Tabela atualizada: Valor a pagar: R${porcentagem}')


    elif renda <= 9564.42:

        porcentagem = (renda * 22.5) / 100
        print('Tabela atualizada: Alíquota 22.5%')
        print(f'Tabela atualizada: Valor a pagar: R${porcentagem}')


    else:
        porcentagem = (renda * 27.5) / 100
        print('Tabela atualizada: Alíquota 27.5%')
        print(f'Tabela atualizada: Valor a pagar: R${porcentagem}')



main()