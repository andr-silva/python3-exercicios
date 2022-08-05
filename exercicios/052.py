# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

number = int(input('Digite um número: '))
total = 0

for counter in range(1, number+1):
    if number % counter == 0:
        print(end='')
        total += 1
    else:
        print(end='')
    
if total == 2:
    print(f'{number} é um número primo!')
else:
    print(f'{number} não é um número primo!')
