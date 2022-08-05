# Faça um programa que tenha uma função notas() que pode receber varias notas de alunos e vai retornar um dicionário com as sequintes informações:
#   Quantidade de notas
#   Maior nota
#   Menor nota
#   A média da turma
#   A situação (opcional)
# Adicione também as docstrings

def average_grade(value, situation=False):

    report = {'Total': len(value), 'Maior Nota': max(value), 'Menor Nota': min(value), 'Média': (sum(value) / len(value))}

    if situation:
        if report['Média'] >= 9:
            report['Situação'] = 'Ótima'
        elif 7 <= report['Média'] < 9:
            report['Situação'] = 'Boa'
        elif 5 <= report['Média'] < 7:
            report['Situação'] = 'Razoável'
        else:
            report['Situação'] = 'Ruim'
            
    return report


grades = [3.1, 5.1, 4.9, 7.9]

print(average_grade(grades, situation=True))
