#8Para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
#depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
#11% do salário bruto, mas não é descontado (é a empresa que deposita). 
# O salário líquido corresponde ao salário bruto menos os descontos.
#  O programa deverá pedir ao usuário o valor da sua hora e a
#quantidade de horas trabalhadas no mês.

def main():
    v_hora = int(input('Qual o valor de sua hora?: '))
    horas_mes = int(input('Quantas horas você trabalhou esse mês?: '))
    
    salario_bruto = v_hora * horas_mes
    calc_salario_liquido(v_hora, horas_mes,salario_bruto)
    fgts(v_hora,horas_mes,salario_bruto)
    sindicato(v_hora,horas_mes,salario_bruto)


def calc_salario_liquido(v_hora, horas_mes,salario_bruto):

    if salario_bruto <= 900:
        inss = (salario_bruto * 10) / 100
        salario_liquido = (salario_bruto - inss)
        print(f'Seu salário liquido é R$ {salario_liquido}')


    elif salario_bruto > 900 and salario_bruto <= 1.500:
        ir = (salario_bruto * 5) / 100
        inss = (salario_bruto * 10) / 100
        salario_liquido = (salario_bruto - inss - ir)
        print (f'Seu desconto é de {salario_liquido}')

    elif salario_bruto > 1.500 and salario_bruto <= 2.500:
        ir = (salario_bruto * 10) / 100
        inss = (salario_bruto * 10) / 100
        salario_liquido = (salario_bruto - inss - ir)
        print (f'Seu desconto é de {salario_liquido}')

    elif salario_bruto > 2.500:
        ir = (salario_bruto * 20) / 100
        inss = (salario_bruto * 10) / 100
        salario_liquido = (salario_bruto - inss - ir)
        print (f'Seu desconto é de {salario_liquido}')


def fgts(v_hora,horas_mes,salario_bruto):

    calc_fgts = (salario_bruto * 11) / 100
    print(f'Será depositado em seu FGTS R$: {calc_fgts}')

def sindicato(v_hora,horas_mes,salario_bruto):

    sindicato = (salario_bruto * 3 / 100)
    print(f'O sindicato receberá: R$: {sindicato}')

main()