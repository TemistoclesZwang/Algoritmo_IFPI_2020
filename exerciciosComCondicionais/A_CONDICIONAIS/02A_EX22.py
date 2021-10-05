### 22. Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras:
# hora e minuto).Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo
# máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia
# seguinte.


def main():
    # hora minuto
    hora_inicio = int(input('Insira a hora de início do jogo: '))
    min_inicio = int(input('Insira os minutos de início do jogo: '))

    hora_fim = int(input('Insira a hora de fim do jogo: '))
    min_fim = int(input('Insira os minutos de fim do jogo: '))

    duracao_hora(hora_inicio, hora_fim, min_inicio, min_fim)
    duracao_min(min_inicio, min_fim)


def duracao_hora(hora_inicio, hora_fim, min_inicio, min_fim):

    if hora_inicio > hora_fim:
        calc_h = hora_inicio - hora_fim
        calc_m = (min_inicio + min_fim) % calc_h

        total_hora = calc_h + calc_m
        print(total_hora, end=':')

    elif hora_fim > hora_inicio:
        calc_h = hora_fim - hora_inicio
        calc_m = (min_inicio + min_fim) % calc_h

        total_hora = calc_h + calc_m
        print(total_hora, end=':')


def duracao_min(min_inicio, min_fim):

    if min_inicio == min_fim:
        calc_min = 00
        print(calc_min)

    elif min_inicio > min_fim:
        calc_min = min_inicio - min_fim
        print(calc_min)

    elif min_fim > min_inicio:
        calc_min = min_fim - min_inicio
        print(calc_min)


main()
