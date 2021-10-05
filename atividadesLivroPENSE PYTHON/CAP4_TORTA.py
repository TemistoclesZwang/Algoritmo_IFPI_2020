import math
import turtle


def desenhar(t, n, r):

    polypie(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()


def polypie(t, n, r):
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        t.lt(angle)


def isosceles(t, r, angle):
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)

tamanho = float(input('Insira o tamanho que deseja: '))
lados = int(input('Insira o tamanho de lados: '))

bob = turtle.Turtle()

bob.pu()
bob.bk(130)
bob.pd()


desenhar(bob, lados, tamanho)




bob.hideturtle()
turtle.mainloop()