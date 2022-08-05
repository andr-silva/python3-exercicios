# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angle = float(input('Digite o ângulo que vodê deseja: '))
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))

print(
    f'O ângulo de {angle}º tem o SENO de {sine:.2f}\n'
    f'O ângulo de {angle}º tem o COSSENO de {cosine:.2f}\n'
    f'O ângulo de {angle}º tem a TAGENTE de {tangent:.2f}'
)
