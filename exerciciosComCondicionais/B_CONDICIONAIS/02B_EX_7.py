#As  Organizações  Tabajara  resolveram  dar  um  aumento  de  salário  aos  seus  colaboradores 
#  e  lhe contrataram para desenvolver o programa que calculará os reajustes.
# Escreva um algoritmoque leiao salário de um colaborador e o reajuste segundo o seguinte critério, 

# baseado no salário atual:osalários até R$ 280,00 (incluindo) : aumento de 20%
# osalários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# osalários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#osalários de R$ 1500,00 em diante : aumento de 5%

# Após o aumento ser realizado, informe na tela:
# ·o salário antes do reajuste;·o percentual de aumento aplicado;·o valor do aumento;·o novo salário, após o aumento.


def main():
    salario = float(input('Insira seu salário: '))
    aumento(salario)


def aumento(salario):
    if salario <= 280:
        sa_atual = (20 * salario) / 100
        print(f'Salário antes do reajuste {salario}')
        print(f'Valor do aumento {sa_atual}')
        print(f'Salário pós reajuste {sa_atual + salario}')

    elif salario >= 280:
        sa_atual = (15 * salario) / 100
        print(f'Salário antes do reajuste {salario}')
        print(f'Valor do aumento {sa_atual}')
        print(f'Salário pós reajuste {sa_atual + salario}')

    elif salario >= 700:
        sa_atual = (10 * salario) / 100
        print(f'Salário antes do reajuste {salario}')
        print(f'Valor do aumento {sa_atual}')
        print(f'Salário pós reajuste {sa_atual + salario}')

    elif salario >= 1500:
        sa_atual = (5 * salario) / 100
        print(f'Salário antes do reajuste {salario}')
        print(f'Valor do aumento {sa_atual}')
        print(f'Salário pós reajuste {sa_atual + salario}')


main()