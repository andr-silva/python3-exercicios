# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso informado.

larger = 0
smaller = 0

for person in range(1, 6):

    weight = float(input(f'Qual o peso da {person}ª pessoa: '))
    
    if person == 1:
        larger = weight
        smaller = weight
    else:
        if weight > larger:
            larger = weight
        if weight < smaller:
            smaller = weight

print(f'O maior peso recebido foi de {larger:.1f}Kg e o menor foi {smaller:.1f}Kg')
