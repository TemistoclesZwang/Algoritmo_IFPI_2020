#25. Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo deve escrever
#uma mensagem de permissão de acesso ou não.


def main():
    senha = input('Digite uma senha: ')
    verificar(senha)


def verificar(senha):
    import string

    alfabeto = list(string.ascii_lowercase)


    for digito in alfabeto:
        if digito in senha:
            print('Senha aceita. Tem letras')
            

    if senha not in alfabeto:
        print('Senha inválida, precisa utilizar letras')
        
    if senha == 1234:
        print('Você não deve utilizar números em sequência.')


main()