# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se ja passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempe que falta ou que passou do prazo.

from datetime import date

year = int(input('Em que ano você nasceu? '))
current_age = date.today().year- year
year_of_enlistment = year + 18

if current_age  == 18:
    print(f'Voce tem que se alistar este ano.')
elif current_age <= 18:
    print(f'Voce tem que se alistar em {year_of_enlistment}.')
else:
    print(f'Você deveria ter se alistado em {year_of_enlistment}.')
