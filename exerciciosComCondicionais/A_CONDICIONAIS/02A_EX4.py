# 4. Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente


def main():
    num = int(input('Insira um número de dois dígitos: '))
    verificar(num)


def verificar(num):
    num1 = (num % 100) // 10  # Digito 1
    num2 = ((num % 100) % 10)  # Digito 2
    print(num1)
    print(num2)

    if num1 == num2:
        print('Os algarismos são iguais.')
    else:
        print('Os algarismos são diferentes.')


main()
