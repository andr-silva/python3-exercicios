# Melhore o exercício 061, perguntando para o usuário se ele quer te mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

first_term = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
progression = 1
total = 0
more = 10

while more != 0:

    total += more

    while progression <= total:

        print(f'{first_term} → ', end='')

        first_term += reason
        progression += 1

    print('PAUSA')

    more = int(input('Quantos termos você quer mostrar a mais?  [0] para finalizar: '))

print(f'Progressao finalizada com {total} termos.')
