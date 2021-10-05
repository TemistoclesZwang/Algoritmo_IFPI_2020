import turtle

t = turtle.Turtle()

def linha(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arco(t, r, angle):
    arco_length = 2 * 2.14 * r * abs(angle) / 360
    n = int(arco_length / 4) + 3
    step_length = arco_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    linha(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def desenhar(t, r):
    arco(t, r, 360)

desenhar(t,2)