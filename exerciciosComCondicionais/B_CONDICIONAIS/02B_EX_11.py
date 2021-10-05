#Leia  um  número  inteiro  menor  que  1000  e  imprima  a  quantidade  de  centenas,  
# dezenas  e  unidades  do número. Observando os termos no plural a 
# colocação do "e", da vírgula entre outros.
# Exemplos:o326 = 3 centenas, 2 dezenas e 6 unidadeso 12 = 1 dezena e 2 unidades


def main():
    num = int(input('Insira um número: '))
    verificar(num)


def verificar(num):
    centena = ((num // 100) % 100) % 10
    dezena = (num % 100) // 10
    unidade = ((num % 100) % 10)

    if unidade > 1:
        print (f'{unidade} unidades')
    elif unidade <=1:
        print (f'{unidade} unidade')

    if centena > 1:
            print (f'{centena} centenas')
    elif centena <=1:
            print (f'{centena} centena')

    if dezena > 1:
            print (f'{dezena} dezenas')
    elif dezena <=1:
            print (f'{dezena} dezena')

main()
