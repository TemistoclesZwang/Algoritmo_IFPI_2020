'''30. Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos
o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo
milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste
terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
2025 -> dividindo: 20 e 25 -> somando temos 45 -> 452 = 2025.
'''

def main():
    num = int(input('Insira um número entre 1000 e 9999: '))
    verificar(num)


def verificar(num):
    milhar = (num // 1000)
    centena = ((num // 100) % 100) % 10
    dezena = (num % 100) // 10
    unidade = ((num % 100) % 10)

    soma1 = milhar + centena
    soma2 = dezena + unidade
    soma3 = (soma1 + soma2) ** 2

    print(soma3)

    

main()