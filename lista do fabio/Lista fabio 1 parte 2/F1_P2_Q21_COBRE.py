# 21 Sabendo que latão é constituído de 70% de cobre e 30% de zinco,
# escreva um algoritmo que calcule a quantidade de cada um desses componentes
# para se obter certa quantidade de latão (em kg), informada pelo usuário.


# ENTRADA
quilo = int(input('Insira o quilo do latão: '))

# PROCESSAMENTO
cobre = (quilo / 100) * 700
zinco = (quilo / 100) * 300

# SAIDA
print(f'Sua quantia em latão representa {cobre}% cobre e {zinco}% zinco')
