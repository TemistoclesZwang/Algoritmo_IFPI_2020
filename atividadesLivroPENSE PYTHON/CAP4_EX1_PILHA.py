import turtle

t = turtle.Turtle()

def linha(t, n, length, angulo):
    for i in range(n):
        t.fd(length)
        t.lt(angulo)
    print('Função linha foi chamada')

def arco(t, r, angulo):
    arco_length = 2 * 2.14 * r * abs(angulo) / 360
    n = int(arco_length / 4) + 3
    step_length = arco_length / n
    step_angulo = float(angulo) / n
    print('A função arco foi chamada, recebendo turtle, raio e ângulo como parâmetro')

    t.lt(step_angulo/2)
    linha(t, n, step_length, step_angulo)
    t.rt(step_angulo/2)


def desenhar(t, r):
    arco(t, r, 360)
    print('A função desenhar foi chamada. Recebendo turtle e raio como parâmetros. E chamando a função arco')

desenhar(t,120)
print('O desenho foi feito')