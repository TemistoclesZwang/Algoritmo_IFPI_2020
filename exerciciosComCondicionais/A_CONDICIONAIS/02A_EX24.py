#24. Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes. Vale lembrar que o
#coeficiente A deve ser diferente de 0 (zero).

def main():
    a = int(input(' Insira o coeficiente A: '))
    b = int(input(' Insira o coeficiente B: '))
    c = int(input(' Insira o coeficiente C: '))
    verificar(a,b,c)


def verificar(a,b,c):
    raizA = a ** (1 / 2)
    raizB = b ** (1 / 2)
    raizC = c ** (1 / 2)

    print(f'Raiz de A {raizA:.2f}')
    print(f'Raiz de B {raizB:.2f}')
    print(f'Raiz de C {raizC:.2f}')


main()