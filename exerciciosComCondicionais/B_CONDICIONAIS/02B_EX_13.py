#13.Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a)"Telefonou para a vítima?"b)"Esteve no local do crime?"
# c)"Mora perto da vítima?"d)"Devia para a vítima?"e)"Já trabalhou com a vítima?"
# O algoritmodeve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder  positivamente  a 2questões  ela  deve  ser  classificada  como  "Suspeita", 
#  entre3  e  4  como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def main():
    p1 = input('Telefonou para a vítima?: [S/N]').upper()
    p2 = input('Esteve no local do crime?: [S/N]').upper()
    p3 = input('Mora perto da vítima?: [S/N]').upper()
    p4 = input('Devia para a vítima: [S/N]').upper()
    p5 = input('Já trabalhou com a vítima: [S/N]').upper()
    verificar(p1,p2,p3,p4,p5)


def verificar(p1,p2,p3,p4,p5):
    lista =[]

    if p1 == 'S':
        lista.append(p1)
    elif p1 == 'N':
        pass

    if p2 == 'S':
        lista.append(p2)
    elif p2 == 'N':
        pass

    if p3 == 'S':
        lista.append(p3)
    elif p3 == 'N':
        pass

    if p4 == 'S':
        lista.append(p4)
    elif p4 == 'N':
        pass

    if p5 == 'S':
        lista.append(p5)
    elif p5 == 'N':
        pass

    if len(lista) >= 2:
        print('Suspeito')
    elif len(lista) <= 1:
        print('Você  é inocente.')

    print (f'Você teve {len(lista)} respostas posivitas.')


main()

