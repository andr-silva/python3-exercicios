# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média.

first_note = float(input('Primeira nota: '))
second_note = float(input('Segunda nota: '))
average = (first_note + second_note) / 2

print(f'A média entre {first_note} e {second_note} é igual a {average:.1f}.')
