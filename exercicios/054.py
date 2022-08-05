# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores.

from datetime import date

current = date.today().year
greater_total = 0
lower_total = 0

for person in range(1, 8):

    birth_date = int(input(f'Em que ano a {person}ª pessoa nasceu?' ))
    age = current - birth_date

    if age >= 18:
        greater_total += 1
    else:
        lower_total += 1

print(f'Ao todo foram listadas {greater_total} pessoas maiores de idade e {lower_total} pessoas menores de idade.')
