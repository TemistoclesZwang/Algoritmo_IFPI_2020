#Altere do_twice para que receba dois argumentos, um objeto de função e um valor, e
#chame a função duas vezes, passando o valor como um argumento.

def do_twice(a,valor):
    a()
    valor()

def teste ():
    print('0 e 1')

do_twice(teste,teste)