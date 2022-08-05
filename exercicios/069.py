# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.

total_18 = total_g1 = total_g2 = total_g3 = total_g4 = 0

while True:

    name = input('Nome: ').title().strip()
    age = int(input('Idade: '))

    while True:

        gender = int(input(
            '[1] Feminino [2] Masculino [3] Outro [4] Prefiro não dizer\n'
            'Gênero: '))

        if gender == 1:
            gender = 'Feminino'
            total_g1 += 1
            break

        elif gender == 2:
            gender = 'Masculino'
            total_g2 += 1
            break

        elif gender == 3:
            gender = str(input('Defina seu gênero: '))
            total_g3 += 1
            break

        elif gender == 4:
            gender = 'Não informado'
            total_g4 += 1
            break

        else:
            print('opção invalida')

    if age >= 18:
        total_18 += 1

    print(f'{name} - {age} - {gender}\nCadastrado!')

    new = input('Novo cadastro? [S] [N] ').upper().strip()[0]

    if new == 'N':
        break


if total_18 <= 1:
    plural = ['', '']
else:
    plural = ['s', 'es']

if total_g3 <= 1:
    plural_3 = ''
else:
    plural_3 = 's'

if total_g4 <= 1:
    plural_4 = ''
else:
    plural_4 = 'ram'

print(f'No total temos {total_18} pessoa{plural[0]} maior{plural[1]} de idade.\n'
      f'{total_g1} do gênero feminino.\n'
      f'{total_g2} do gênero masculino.\n'
      f'{total_g3} de Outro{plural_3} gênero{plural_3} .\n'
      f'{total_g4} Não disse{plural_4}.\n')
