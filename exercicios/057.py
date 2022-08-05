# faça um programa que leia o sexo de uma pessoa, e só aceite "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

gender = str(input('[1] Feminino [2] Masculino [3] Outro [4] Prefiro não dizer\n'
                   'Gênero: '))

while gender not in ['1', '2', '3',' 4']:
    gender = str(input('[1] Feminino [2] Masculino [3] Outro [4] Prefiro não dizer\n'
                       'opção inválida, escolha o seu gênero: '))

if gender == '1':
    gender = 'Feminino'
elif gender == '2':
    gender = 'Masculino'
elif gender == '3':
    gender = str(input('Defina seu gênero: '))
elif gender == '4':
    gender = 'Não informado'

print(f'Genêro {gender} registrado!')
