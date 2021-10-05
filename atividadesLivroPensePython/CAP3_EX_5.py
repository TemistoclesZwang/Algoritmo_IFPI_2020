'''Defina uma função nova chamada do_four que receba um objeto de função e um
valor e chame a função quatro vezes, passando o valor como um parâmetro. Deve
haver só duas afirmações no corpo desta função, não quatro.'''

def do_four(f,valor):
    f(),valor
    f(),valor


def teste():
    print ('T E S T E')
    print ('T E S T E')


do_four(teste,teste)