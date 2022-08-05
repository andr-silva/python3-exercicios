# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente,
# Ex: Ana Maria de Souza
#   primeiro = Ana
#   ultimo = Souza

name = str(input('Qual seu nome completo? ')).strip()
first_name = name.split()[0]
last_name = name.split()[len(name.split())-1]

print(
    f'Seu primeiro nome é {first_name}\n'
    f'Seu último nome é {last_name}'
)
