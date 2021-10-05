#3 Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro
#chamado n e altere o corpo para que desenhe um polígono regular de n.

import turtle


tamanho = int(input('Insira o tamanho: '))
t = turtle.Turtle()

def polygon(t,tamanho,n):
    t.fd(tamanho) # Traça a linha
    t.lt(n) #Vira a seta
    t.fd(tamanho)
    t.lt(n)
    t.fd(tamanho)
    t.lt(n)
    t.fd(tamanho)
    t.lt(n)
    t.fd(tamanho)
    t.lt(n)
    t.fd(tamanho)
    turtle.mainloop()
    

polygon(t,tamanho,60)
