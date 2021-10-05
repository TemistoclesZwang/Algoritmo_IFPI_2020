#Escreva uma função chamada square que receba um parâmetro chamado t, que é um
#turtle. Ela deve usar o turtle para desenhar um quadrado.
import turtle

t = turtle.Turtle()

def square(t):
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    turtle.mainloop()
    

square(t)