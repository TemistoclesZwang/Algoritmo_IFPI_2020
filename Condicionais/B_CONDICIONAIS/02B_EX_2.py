#Leia uma letra,verifique se  letra é "F" ou "M" e escreva F -Feminino, M -Masculino, Sexo Inválido.

def main():
    letra = input('Insira uma letra: ').lower() #Transforma para minúsculo. Assim não importa o que o usuário digitar.
    verificar(letra)


def verificar(letra):
    if letra == 'f':
        print('Feminino')

    elif letra == 'm':
        print('Masculino')

    elif letra != 'f' or 'm':
        print('Sexo inválido')


main()