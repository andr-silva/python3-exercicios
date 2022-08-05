

def border(length = 40, format='-'):
    return format * length


def header(title, length = 40, format='-'):

    print(
        f'{border(length,format)}\n'
        f'{title.center(length)}\n'
        f'{border(length,format)}'
    )

def main_menu(title, list_options):
        

    from lib.input_verify import check_int

    header(title)

    count = 1

    for option in list_options:
        print(f'{count} - {option}')
        count += 1

    print(border())

    option = check_int('Opção: ')
    return option
