# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostr sua categoria, de acordo com a idade:
#   Até 9 anos: MIRIM
#   Até 14 anos: INFANTIL
#   Até 19 anos: JUNIOR
#   Até 25 anos: SÊnior
#   Acima: MASTER

from datetime import date
year = int(input('Qual ano de nascimento? '))
age = date.today().year - year

if age <= 9:
    classification = 'MIRIM'
elif age <= 14:
    classification = 'INFANTIL'
elif age <= 19:
    classification = 'JUNIOR'
elif age <= 25:
    classification = 'SÊNIOR'
else:
    classification = 'MASTER'

print(
    f'O atleta tem {age} anos\n'
    f'Classificação: {classification}'
)
