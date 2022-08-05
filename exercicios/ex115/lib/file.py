def browse_file(value):

    try:
        with open(value,'rt') as cadastro:
        
            print(f'Arquivo exitente')


    except FileNotFoundError:
        return False
    else:
        return True


def create_file(value):

    if  not browse_file(value):

        with open(value,'wt+'):
            print('Arquivo criado com sucesso!')
    


def read_file(value):

        with open(value,'rt') as file:
            for line in file:
                data = line.split(';')
                data[(len(data) - 1)] = data[(len(data) - 1)].replace('\n','')

                print(f'{data[0]:<20} {data[1]:>5} {data[2]:>14}')



def insert_in_file(file,name, age, gender):

    with open(file,'at') as a:
        a.write(f'{name.title()};{age};{gender}\n')
        print(f'Novo registo: {name}')
