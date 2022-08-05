# Faça um programa que tenha uma função chamada área(), que receba as dimeçoes de um terreno retangular(largura e comprimento) e mostre a área do terreno.

def area(width, length):
    
    return width * length


def area_description(width, length):

    a = width * length
    print(f'A Área de {width}m x {length}m é igual a {a}m²')


wh = float(input('Largura: '))
lh = float(input('COmprimento: '))

print(area(wh, lh))

area_description(wh, lh)
