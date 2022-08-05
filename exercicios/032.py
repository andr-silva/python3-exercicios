# faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

age = int(input('Qual o ano? (0 para ano atual) '))

if age == 0:
    age = date.today().year
if age % 4 == 0 and age % 100 != 0 or age % 400 == 0:
    print(f'{age} é bissexto')
else:
    print(f'{age} não é bissexto')
