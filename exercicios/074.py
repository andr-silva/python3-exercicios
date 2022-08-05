# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e maior valor que estão na tupla.

from random import randint, sample

numbers = (randint(1, 99), randint(1, 99), randint(1, 99), randint(1, 99), randint(1, 99))

print(
    f'Os números sorteados foram {numbers}\n'
    f'{min(numbers)} é o menor da tupla e {max(numbers)} é o maior.'
)

# outra forma
numbers_2 = tuple(sample(range(1, 99), 5))

print(
    '\nOutra forma\n'
    f'Os números sorteados foram {numbers_2}\n'
    f'{min(numbers_2)} é o menor da tupla e {max(numbers_2)} é o maior.'
)
