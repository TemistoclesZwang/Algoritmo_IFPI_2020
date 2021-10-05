#20. Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou
#quarto) em que o ângulo se localiza.

def main():

    angulo = int(input("Angulo: "))
    quadrante (angulo)



def quadrante (angulo):
    if angulo >= 0 and angulo < 90:
        print('1º quadrante')

    elif angulo >= 90 and angulo < 180:
        print('2º quadrante')

    elif angulo >= 180 and angulo < 270:
        print('3º quadrante')

    elif angulo >= 270 and angulo < 360:
        print('4º qudrante')
        
    else:
        print('Erro. Insira um ângulo entre 0 e 360')



main()
