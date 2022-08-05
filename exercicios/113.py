# Reescreva a função leiaInt() que fizemos no exercício 104, incluindo agoa a possibilidade de digitação de um número de tipo inválido. Aproveite e crie tambem uma função leiaFloar() com a mesma funcionalidade.

def error_alert(value):

    alert = {
        'ValueError_int':'ERRO, digite um número inteiro válido.',
        'ValueError_float':'ERRO, digite um número real válido.',
        'KeyboardError':'\nO programa foi encerrado via teclado.'
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


test = check_int('Digite um número inteiro: ')
test_2 = check_float('Digite um número real: ')

print(
    f'O inteiro digitado foi {test}\n'
    f'O real digitado foi {test_2}'
)
