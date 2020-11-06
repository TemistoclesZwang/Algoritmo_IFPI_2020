#16. Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior
#ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média
#final. Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve
#escreva “Reprovado”.

def main():
    nota1 = int(input('Insira a nota 1: '))
    nota2 = int(input('Insira a nota 2: '))
    media (nota1, nota2)


def media(nota1,nota2):
    soma = (nota1 + nota2) / 2
    if soma >= 7:
        print (f'Sua média é {soma}. Você está aprovado.')
    elif soma <= 7:
        print (f'Sua média é {soma}. Você precisar fazer o exame final.')
        exame_final = int(input('Insira sua nota do exame final: '))
        if exame_final <= 5:
            print('Você está reprovado =(')
        else:
            print('Você está aprovado! =)')

main()
