# 20. Um sistema de equações lineares do tipo , pode ser resolvido segundo mostrado abaixo:

# ENTRADA
a = int(input('Insira o coeficiente a: '))
b = int(input('Insira o coeficiente b: '))
c = int(input('Insira o coeficiente c: '))
d = int(input('Insira o coeficiente d: '))
e = int(input('Insira o coeficiente e: '))
f = int(input('Insira o coeficiente f: '))

# PROCESSAMENTO
calc1 = (c * e) - (b * f)
calc2 = (a * e) - (b * d)

x = calc1 / calc2

calc3 = (a * f) - (c * d)
calc4 = (a * e) - (b * d)

y = calc3 / calc4

# SAIDA
print (f'X é igual a: {x}')
print (f'Y é igual a: {y}')
