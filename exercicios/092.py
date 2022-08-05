# Crie um programa que leia, nome, ano de nascimento e carteira de tranalho e cadastre-os (com idade) em um dicionario , se por acaso a CTPS for diferente de ZERO, o dicionário receberá tambem o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai aposentar.

from datetime import datetime

worker = {
    'Nome': str(input('Nome: ')).title().strip(),
    'Idade': datetime.now().year - (int(input('Ano do nascimento: ')))
}

work_card_number = input('Número da carteira de trabalho (enter vazio nao tem): ')
border = '-' * 40

if work_card_number == '':
    worker['Carteira de trabalho'] = 'Não possui'
else:
    worker['Carteira de trabalho'] = int(work_card_number)
    worker['Adimissão'] = int(input('Ano da admissão: '))
    worker['Salário'] = float(input('Salário: '))
    worker['Aposentadoria'] = worker['Idade'] + ((worker['Adimissão'] + 35) - datetime.now().year)

print(border)

for key, value in worker.items():
    print(f'{key}: {value}')

print(border)
