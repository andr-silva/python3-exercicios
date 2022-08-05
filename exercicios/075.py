# Desenvolva um programa que receba quatro valores e guarde-os em uma tupla. No final mostre:

numbers = (
    int(input('[1/4] Digite um número: ')),
    int(input('[2/4] Digite outro número: ')),
    int(input('[3/4] Digite outro número: ')),
    int(input('[4/4] Digite outro número: '))
    )

pair_counter = 0


if 9 in numbers:

    count = numbers.count(9)

    if count == 1:        
        result_9 = f'{count} vez'

    elif count > 1:
        result_9 = f'{count}vezes'

else:
        result_9 = 'nenhuma vez'


if 3 in numbers:
    position = numbers.index(3)+1

    result_3 =  f'na {position}ª'

else:
    result_3 = 'nenhuma vez'

print(
    f'Os valores digitados foram {numbers}\n'
    f'O número 3 apareceu {result_3}.\n'
    f'o valor 9 apareceu {result_9} na pupla.\n'
    'Os valores pares foram: ', end=''
)

for number in numbers:

    if number % 2 == 0:
        pair_counter += 1

        print(f'{number}', end=" ")
    
if pair_counter == 0:
    print('Nenhum')
