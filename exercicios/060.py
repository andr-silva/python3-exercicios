# Faça um programa que leia um número qualquer e mostre o seu fatorial.

number = int(input('Digite o número: '))
count =  number
factorial = 1

print(f'Calculando {number}! = ', end='')

while count > 0:
    print(f'{count}', end='')
    print(' x ' if count > 1 else ' = ', end='')
    factorial *= count
    count -= 1

print(factorial)
