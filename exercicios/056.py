# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do Homem mais velho.
# Qunatas mulheres tem menos de 20 anos.

names = []
ages = []
sexes = []
of_age = 0
soma = 0
cont = 0

for person in range(1, 5):
    print(f'{person}ª Pessoa')

    name = str(input('Nome: '))
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip().upper()

    names.append(name)
    ages.append(age)
    sexes.append(sex)

    if sex == "M":
        if person == 1:
            age_index = person - 1
            of_age = age
        else:
            if age > of_age:
                age_index = person - 1
                of_age = age

    if sex == "F":
        if age < 20:
            cont += 1
    soma += age

average = soma / person

if cont > 1:
    plural_1 = "são"
    plural_2 = 'es'
else:
    plural_1 = "é"
    plural_2 = ""

print(f'A média de idade do grupo é de {average} anos\n'
      f'O homem mais velho tem {ages[age_index]} anos e se chama {names[age_index]}\n'
      f'Ao todo {plural_1} {cont} mulher{plural_2} com menos de 20 anos')
