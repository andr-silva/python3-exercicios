# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando o valor liteal indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def vote(value):

    from datetime import date

    age = date.today().year - value

    if age < 16:
        return f'Com {age} anos não pode votar.'
    elif 16 <= age < 18 or age > 65:
        return f'Com {age} anos voto é opcional'
    else:
        return f'Com {age} anos o voto é obrigatório.'


year = int(input('Ano que nasceu: '))

print(vote(year))
