# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#   Ex: 1 → 1 → 2 → 3 → 5 → 8

print('=-=- Sequência de Fibonacci -=-=')

number = int(input('Quantos termos você quer mostrar: '))
term_1 = 0
term_2 = 1
counter = 3

print(f'{term_1} → {term_2} → ', end='')

while counter <= number:

    term_3 = term_1 + term_2

    print(f'{term_3} ', end='')
    print(' → ' if counter < number  else '\n', end='')

    term_1 = term_2
    term_2 = term_3
    counter += 1
