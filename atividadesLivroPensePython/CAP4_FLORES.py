import turtle

def arco(t, r, angle):
    arco_length = 2 * 2.14 * r * abs(angle) / 360
    n = int(arco_length / 4) + 3
    step_length = arco_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    #linha(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def petal(t, r, angle):
    for i in range(2):
        arco(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)


def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Turtle()

move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.mainloop()
