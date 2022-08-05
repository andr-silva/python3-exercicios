# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n_1 = float(input('Digite um numero: '))
n_2 = float(input('Digite um numero: '))
n_3 = float(input('Digite um numero: '))

list_of_numbers = [n_1, n_2, n_3]

bigger = max(list_of_numbers)
little = min(list_of_numbers)

print(
    f'O menor numero é {little}\n'
    f'O maior numero é {bigger}'
)
