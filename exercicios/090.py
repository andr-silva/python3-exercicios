# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, nostreo consteúdo da estrutura na tela.

student = {'nome': str(input('Nome: ')),
           'média': float(input('Média: '))}

if student['média'] < 0 or student['média'] > 10:
    student['situacao'] = 'Valor invalido'
elif student['média'] >= 7:
    student['situacao'] = 'Aprovado'
elif 5 <= student['média'] < 7:
    student['situacao'] = 'Recuperação'
else:
    student['situacao'] = 'Reprovado'

if 12 + (len(student['situacao'])) > 8 + (len(student['nome'])):
    formt = ('-' * (12 + (len(student['situacao']))))
else:
    formt = ('-' * (8 + (len(student['nome']))))

print(formt)

for key, value in student.items():
    print(f'{key.title()}: {value} ')

print(formt)
