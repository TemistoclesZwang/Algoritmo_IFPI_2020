# Leia2 (duas) notas parciais de um aluno, calcule a média eescreva a mensagem:
# o"Aprovado", se a média alcançada for maior ou igual a sete;o"Reprovado",
# se a média for menor do que sete;o"Aprovado com Distinção", se a média for igual a dez.


def main():
    nota1 = int(input('Insira a nota 1: '))
    nota2 = int(input('Insira a nota 2: '))
    verificar(nota1, nota2)


def verificar(nota1, nota2):
    calc = (nota1+nota2) / 2

    if calc >= 7:
        print(f'Sua média é {calc} você foi aprovado.')

    elif calc <= 7:
        print(f'Sua média é {calc} você foi reprovado.')

    elif calc == 10:
        print('Sua média foi 10. Você foi aprovado com distinção!')


main()
