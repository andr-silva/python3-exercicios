# Refaça o exercício 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

first_term = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
progression = 1

while progression <= 10:

    print(f'{first_term} → ', end='')

    first_term += reason
    progression += 1

print('Fim')
