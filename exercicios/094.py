# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados.py de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#   Quantas pessoas cadastradas.
#   A média de idade.
#   uma lista com mulheres.
#   uma lista com idade acima da média.

person = {}
people = []
ages = 0

border = '-' * 40

while True:

    print(border)

    if len(people) == 1:
        print('Vazio para finalizar')
    name = input('Nome: ').title().strip()

    if name == '':
        break

    person['Nome'] = name

    while True:

        age = input('Idade: ')

        if age.isnumeric():
            age = int(age)
            person['Idade'] = age
            ages += age
            break
        else:
            print('Tente novamente.')

    while True:

        gender = int(input(
            '[1] Feminino   [2] Masculino\n'
            '[3] Outro      [4] Prefiro não dizer\n'
            'Gênero: '))

        if gender == 1:
            person['Gênero'] = 'Feminino'
            break
        elif gender == 2:
            person['Gênero'] = 'Masculino'
            break
        elif gender == 3:
            person['Gênero'] = str(input('Defina seu gênero: '))
            break
        elif gender == 4:
            person['Gênero'] = 'Não informado'
            break
        else:
            print('opção invalida')

    people.append(person.copy())
    person.clear()

total_pessoas = len(people)
pl = '' if total_pessoas <= 1 else 's'
media_idades = ages / total_pessoas

print(
    f'{total_pessoas} pessoa{pl} cadastrada{pl}.\n'
    f'A média da idade é de {media_idades:.1f} anos\n'
    'Pessoas que não informaram o gênero:'
)

for value in people:

    if value['Gênero'] == 'Não informado':
        print(f'   {value["Nome"]} {value["Idade"]} anos')

print('Lista de pessoas acima da média:')

for value in people:

    if value['Idade'] >= media_idades:

        print(border)

        for key, dados in value.items():
            print('   ', end='')
            print(f'{key}: {dados}')

print(border)
