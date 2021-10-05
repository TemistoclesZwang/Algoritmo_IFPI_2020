#Leia o turno em que um aluno estuda, sendoM para matutino,Vpara Vespertino ou NparaNoturno
# e escrevaa mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def main():
    turno = input('Qual seu turno?[M/V/N]:').upper() #Para transformar em maiúsculas
    verificar(turno)


def verificar(turno):
    if turno == 'M':
        print('Bom dia!')

    if turno == 'V':
        print('Boa tarde!')

    if turno == 'N':
        print('Boa noite')
    else:
        print('Digite de acordo com a legenda: sendo M para matutino,V para Vespertino ou N para Noturno')
        
        
main()