#19. Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea
#(IMC = peso / altura2

def main():
    altura = float (input('Insira sua altura (não use vírgula. Use ponto.): '))
    peso = float (input('Insira seu peso: '))
    imc(altura,peso)

def imc(altura,peso):
    calc = peso /(altura * altura)
    print(f'Seu IMC é: {calc:.2f}')

    if calc < 25:
        print('Seu peso está normal.')

    elif calc >= 25 and calc <= 30:
        print('Você está obeso, precisa emagrecer.')

    elif calc > 30:
        print('Você precisa procurar um médico. Está com obesidade mórbida.')

main()

