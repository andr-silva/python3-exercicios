# Faça um programa que tenha uma função chamada contador (), que receba três parâmetros: início, fim, passo. Seu programa tem que realizar três contagens atraves da função criada:
#   De 1 até 10, de 1 em 1.
#   De 10 até 0, de 2 em 2.
#   Uma contagem personalizada.

def count_numbers(first_number, last_number, jump):

    print(f'Contagem de {first_number} até {last_number} de {jump} em {jump}:')

    if first_number < last_number:
        for numbers in range(first_number, last_number+1, jump):
            print(numbers, end=' ')
    else:
        for numbers in range(first_number, last_number+1, -jump):
            print(numbers, end=' ')

    print('\n')


count_numbers(1, 10, 1)
count_numbers(100, 1, 5)

print('Agora é sua vez de personalizar a contagem!')

first = int(input('Início: '))
last = int(input('Fim: '))
jump = int(input('Passo: '))

count_numbers(first, last, jump)
