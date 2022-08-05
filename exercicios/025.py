# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual o seu nome completo? ')).strip().upper()
checker = "SILVA" in nome

print(f'Seu nome tem Silva? {checker}')
