#Leiauma letra e verifique se a letra digitada é vogal ou consoante

def main():
    letra = input('Digite uma letra: ').lower()
    verificar(letra)

def verificar(letra):
    vogais = 'a','e', 'i', 'o', 'u'

    if letra == vogais:
        print(f'{letra} É uma vogal!')

    elif letra != vogais:
        print(f'{letra} É uma consoante!')


main()