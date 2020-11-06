def façauma(f):
    f()
def façaquatro(f):
    f(),f(),f(),f()
def façatres(f):
    f(),f(),f()

def inicio():
    print('+', ' -'*8, '+', end='')
    print(' -'*8, ' +')


def meio():
    print('|', ' '*16, '|', ' '*16, '|')

def linha_meio():
    print('+', ' -'*8, '+', ' -'*8, '+')


def fim():
    print('+', ' -'*8, '+', end='')
    print(' -'*8, ' +')


façauma(inicio)
façaquatro(meio)
façauma(linha_meio)
façatres(meio)
façauma(fim)
