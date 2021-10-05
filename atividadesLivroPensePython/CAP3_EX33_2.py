def faça_quatro(f):
    f()
    f()
    f()
    f()

def horizontal_inicio():
    inicio = print('+', '-'*8, ' +', '-'*8, '+', '-'*8, '+', '-'*8, '+')

def horizontal_fim():
    fim = print('+', '-'*8, ' +', '-'*8, '+', '-'*8, '+', '-'*8, '+')

def criar():
    inicio = print('+', '-'*8, '+ ', '-'*8, '+', '-'*8, '+', '-'*8, '+')
    colunas = print('|',' '*8,'|', ' '*8, '','|',' '*8,'|', ' '*8, '|')
    colunas = print('|',' '*8,'|', ' '*8, '','|',' '*8,'|', ' '*8, '|')
    colunas = print('|',' '*8,'|', ' '*8, '','|',' '*8,'|', ' '*8, '|')


faça_quatro(criar)
horizontal_fim()
