# Crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se o usuário vai continuar. No final, Mostre:

total = total_thousand = smaller = count = 0
cheap = ' '

while True:

    product = str(input('Nome do produto: '))
    price = float(input('Preço: R$ '))
    count += 1
    total += price

    if price >= 1000:
        total_thousand += 1

    if count == 1 or price < smaller:
        smaller = price
        cheap = product

    answer = ' '

    while answer not in 'SN':

        answer = str(input('Incluir novo produto? [S] [N] ')).strip().upper()[0]

    if answer == 'N':
        break


if count == 1:
    plural_1 = ''
else:
    plural_1 = 's'

if total_thousand == 0:
    plural_2 = ['Nenhum', '']
elif total_thousand == 1:
    plural_2 = ['Temos 1 ', '']
else:
    plural = [f'Temos {total_thousand}', 's']

print(
    f'{count} produto{plural_1} cadastrado{plural_1}.\n'
    f'Valor total da compra: R${total:.2f}\n'
    f'{plural_2[0]} produto{plural_2[1]} custando mais de R$1.000,00\n'
    f'{cheap} foi o produto com menor preço custando R$ {smaller:.2f}'
)
