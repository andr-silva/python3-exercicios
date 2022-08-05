from curses.ascii import isalpha


def error_alert(value):

    alert = {
        'ValueError_int':'ERRO! digite um número inteiro válido.',
        'ValueError_float':'ERRO! digite um número real válido.',
        'KeyboardError':'\nO programa foi encerrado via teclado.',
        'ValueError_alpha':'ERRO! digite um nome válido.'
    }

    return alert[value]


def check_int(value):

    while True:
        try:
            number = int(input(value))
        except (ValueError,TypeError):
            print(error_alert('ValueError_int'))
            continue
        except (KeyboardInterrupt):
            print(error_alert('KeyboardError'))
            break
        else:
            return number


def check_float(value):

    while True:
        try:
            number = float(input(value))
        except (ValueError,TypeError):
            print(error_alert('ValueError_float'))
            continue
        except (KeyboardInterrupt):
            print(error_alert('KeyboardError'))
            break
        else:
            return number

def check_alpha(value):

    while True:
        try:
            name = str(input(value))
        except (ValueError,TypeError):
            print(error_alert('ValueError_alpha'))
            continue
        except (KeyboardInterrupt):
            print(error_alert('KeyboardError'))
            break
        else:
            return name


def check_gender():

    while True:

        gender = check_int(
            '[1] Feminino [2] Masculino [3] Outro [4] Prefiro não dizer\n'
            'Gênero: ')

        if gender == 1:
            return 'Feminino'
        elif gender == 2:
            return 'Masculino'
        elif gender == 3:
            return str(input('Defina seu gênero: '))
        elif gender == 4:
            return 'Não informado'        
        else:
            print('Opção inválida')
