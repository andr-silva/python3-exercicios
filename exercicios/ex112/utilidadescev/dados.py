def checker(value):

    valid = False
    is_alpha = f'ERRO "{value}" é um preço inválido'

    while not valid:

        analyzed_value = str(input(value)).replace(',','.').strip()

        if analyzed_value.isalpha() or analyzed_value == '':
            print(is_alpha)
        else:
            valid = True
            return float(analyzed_value) 
            