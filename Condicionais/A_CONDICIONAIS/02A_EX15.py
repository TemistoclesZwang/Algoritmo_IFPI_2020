#15. Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
#Escreva na tela qual dos professores tem salário total maior.


def main():
    professor1 = int(input('insira a quantidade horas/aula do professor 1: '))
    professor2 = int(input('insira a quantidade horas/aula do professor 2: '))

    salario (professor1, professor2)

def salario(professor1,professor2):
    valor_hora = 15

    calculo1 = professor1 * valor_hora
    calculo2 = professor2 *valor_hora

    if calculo1 > calculo2:
        print (f'O professor 1 recebe mais. Totalizando {calculo1}')
    elif calculo2 > calculo1:
        print (f'O professor 2 recebe mais. Totalizando {calculo2}')

main()