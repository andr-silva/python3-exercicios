from lib.interface import *
from lib.file import read_file, insert_in_file
from lib.input_verify import check_int, check_alpha,check_gender


options = ['Cadastrar nova pessoa', 'Listar pessoas cadastradas', 'Sair do Sistema']
file = 'assets/cadastro_pessoas.txt'

while True:
    
    option = main_menu('Menu Princial',options)

    if option == 1:

        header(options[option-1])

        name = check_alpha('Nome: ')
        age = check_int('Idade: ')
        gender = check_gender()

        insert_in_file(file, name, age, gender)

    elif option == 2:

        header(options[option-1])

        print(f'{"Nome":<20} {"Idade"} {"Genêro":>14}')

        read_file(file)

    elif option == 3:

        header('Sistema encerrado.')
        break

    else:

        print('Opção inválida!')
