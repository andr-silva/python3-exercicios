# Faça um programa que leia a largura e altura de uma parede em metros, calcule a área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro  de tinta, pinta uma área de 2m².

width = float(input('largura da parede: '))
height = float(input('Altura da parede: '))
area = width * height
ink = area / 2

print(
    f'Sua parede tem a dimenção de {height}m x {height}m\n'
    f'area de {area:.1f}m²\n'
    f'Para pintar essa parede você precisa de {ink:.1f}l de tinta.'
)
