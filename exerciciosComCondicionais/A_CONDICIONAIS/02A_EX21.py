# 21. Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for
# maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
# contrario, é arredondado para o inteiro imediatamente inferior.


def main():
    numero = float(input('Insira um número do tipo float: '))
    verificar(numero)


def verificar(numero):
    if numero % 1 >= 0.5:
        numero = (numero // 1) + 1
        print(f'Seu número foi arredondado para: {numero}')

    else:
        numero = numero - (numero % 1)
        print(f'Seu número foi arredondado para: {numero}')


main()
