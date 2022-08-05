# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um  triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

opposite = float(input('Comprimento do cateto oposto: '))
adjacent = float(input('Comprimento do cateto adjacente: '))
hypotenuse_1 = (opposite ** 2 + adjacent ** 2) ** (1/2)
hypotenuse_2 = hypot(opposite,adjacent)

print(
    f'A hipotenusa vai medir {hypotenuse_1:.2f}\n'
    f'A hipotenusa vai medir {hypotenuse_2:.2f}'
)
