# Crie um programa que vai lrt vários números e colocar em uma lista. Depois disso, mostre:
#   Quantos números foram digitados.
#   A lista de valores, ordenada de forma descrescente.
#   Se o valor 5 foi digitado e está ou não na lista.

numbers = []
border = '-'*40

while True:

    numbers.append(int(input('Digite um valor: ')))

    while True:

        answer = str(input('Adicionar outro valor?: [S] [N] ')).upper().strip()

        if answer in 'SN':
            break
        else:
            print('Resposta inválida. ', end='')

    if answer == 'N':
        break

numbers.sort(reverse=True)
the_amount = len(numbers)

if 5 in numbers:
    result_5 = ''
else:
    result_5 = 'não'

print(
    f'{border}\n'
    f'Lista criada com {the_amount} valores\n'
    f'Os valores em ordem decrescete são {numbers}\n'
    f'O valor 5 {result_5} foi encontrado na lista.\n',
    f'{border}'
)