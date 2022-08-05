# Crie um programa que leia um numero inteiro e mostre se ele é PAR ou ÍMPAR.

number = int(input('Digite um numero: '))

if number % 2 == 0:
    print(f'{number} é par')
else:
    print(f'{number} é impar')
