# Crie um programa que vai ler vários numeros e colocar em uma lista. Depois disso, crie dias lista extras que vão conter apenas os valores pares e valores ímpares digitados, respectibamente. Ao final, mostre o conteúdo dos três listas geradas.

numbers = []
odd_numbers = []
pair_numbers = []
pl_odd = pl_pair = ['','']

while True:

    answer = input('Digite um valor: : ').strip()

    if answer == '':
        break
    else:
        numbers.append(int(answer))

    if len(numbers) == 1:
        print('Deixe o valor vazio para finalizar!')

for number in numbers:

    if number % 2 == 0:
        pair_numbers.append(number)
    else:
        odd_numbers.append(number)

if len(odd_numbers) == 0:
    result_odd = 'Nenhum'
elif len(odd_numbers) == 1:
    result_odd = 1
else:
    result_odd = len(odd_numbers)
    pl_odd = ['s','es']

if len(pair_numbers) == 0:
    result_pair = 'Nenhum'
elif len(pair_numbers) == 1:
    result_pair = 1
else:
    result_pair = len(pair_numbers)
    pl_pair = ['s','es']

print(
    f'Lista completa: {numbers}\n'
    f'{result_pair} número{pl_pair[0]} par{pl_pair[1]} encontrado{pl_pair[0]} na lista: {pair_numbers}\n'
    f'{result_odd} número{pl_odd[0]} ímpar{pl_odd[1]} encontrado{pl_odd[0]} na lista: {odd_numbers}'
)
