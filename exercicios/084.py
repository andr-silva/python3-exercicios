# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#   Quantas pessoas foram castradas.
#   Uma listadem com as pessoas pesadas.
#   Uma listagem com as pessoas leves.

temporary = []
people = []
heaviest = lighter = 0

while True:
    name = input('Nome: ').strip()
    if name == '':
        break
    temporary.append(name.upper())
    temporary.append(float(input('Peso: ').strip()))

    if len(people) == 0:
        print('Enter com valor vazio para finalizar!')
        heaviest = lighter = temporary[1]
    else:
        if temporary[1] > heaviest:
            heaviest = temporary[1]
        if temporary[1] < lighter:
            lighter = temporary[1]

    people.append(temporary[:])
    temporary.clear()

print(
    f'{len(people)} pessoas cadastrada na lista.\n'
    f'O maior peso foi de {heaviest}Kg', "".join(f'[{name}] ' for name, kg in people if heaviest == kg),'\n'
    f'O menor peso foi de {lighter}Kg', "".join(f'[{name}] ' for name, kg in people if lighter == kg)
)
