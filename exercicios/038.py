# Escreva um programa que leia dois números inteiros e compare-os, mostando na tela uma mensagem:
#   O primeiro valor é maior.
#   O segundo valor é maior.
#   Não existe valor maior, pois os dois são iguais.

number_1 = float(input('Digite um número: '))
number_2 = float(input('Digite outro número: '))

if number_1 > number_2:
    print(f'{number_1} é maior')
elif number_2 > number_1:
    print(f'{number_2} é maior')
else:
    print('Os numeros são iguais')
