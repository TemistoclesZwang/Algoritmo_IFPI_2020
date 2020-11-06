#26. Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.

def main():
    lado1 = int(input('Insira o lado: '))
    lado2 = int(input('Insira o lado: '))
    lado3 = int(input('Insira o lado: '))

    hipotenusa(lado1,lado2,lado3)


def hipotenusa(lado1,lado2,lado3):
    hipo = (lado1 **2) + (lado2 **2) + (lado3 **2)
    print (f'Os catetos são: {lado1},{lado2},{lado3}. Sua hipotenusa é {hipo}')

main()