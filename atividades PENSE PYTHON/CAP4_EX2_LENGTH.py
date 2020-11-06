#Escreva uma função chamada square que receba um parâmetro chamado t, que é um
#turtle. Ela deve usar o turtle para desenhar um quadrado.
import turtle

t = turtle.Turtle()

def square(t,length):
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    turtle.mainloop()
    

square(t,200)