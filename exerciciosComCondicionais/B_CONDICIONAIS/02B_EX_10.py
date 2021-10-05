#Leiaas duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
#  e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

def main():
    nota1 = int(input('Insira a nota 1: '))
    nota2 = int(input('Insira a nota 2: '))
    media(nota1,nota2)


def media(nota1,nota2):
    soma = (nota1 + nota2) / 2
    if soma >= 9:
        print (f'Sua média é {soma}')
        print(f'Sua nota é A')
        print(f'Você foi aprovado. ')

    elif soma >= 7.5:
        print (f'Sua média é {soma}')
        print(f'Sua nota é B')
        print(f'Você foi aprovado. ')

    elif soma >= 6:
        print (f'Sua média é {soma}')
        print(f'Sua nota é C')
        print(f'Você foi aprovado. ')


    elif soma >= 4:
        print (f'Sua média é {soma}')
        print(f'Sua nota é D')
        print(f'Você foi reprovado. ')

    elif soma <= 4:
        print (f'Sua média é {soma}')
        print(f'Sua nota é E')
        print(f'Você foi reprovado. ')


main()