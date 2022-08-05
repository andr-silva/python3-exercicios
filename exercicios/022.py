# Crie um programa que leia o nome completo de uma pessoa e mostre:
#   O nome com todas as letras maiúsculas e minúsculas.
#   Quantas letras ao todo (sem considerar espaços).
#   Quantas letras tem o primeiro nome.

name = str(input('Digite seu nome: ')).strip()
capitalize_name = name.upper()
lowercase_name = name.lower()
replace_name = name.replace(' ', '')
letter_count = len(replace_name)
separate_name = name.split()
first_name = separate_name[0]
first_name_letter_count = len(separate_name[0])

print(
    f'Analisando seu nome...\n'
    f'Em maiúsculo é {capitalize_name}.\n'
    f'Em minúsculo é {lowercase_name}.\n'
    f'Seu nome tem ao todo {letter_count} letras.\n'
    f'Seu primeiro nome é {first_name} e tem {first_name_letter_count} letras.'
)
