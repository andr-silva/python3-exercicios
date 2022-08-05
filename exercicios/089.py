# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim coontendo a média de casa um e permita que o usuário possa mostrar as notas de cada aluno indivitualmente.

students_list = []
border = ('-'*30)

while True:

    student = []
    name = str(input('Nome: ').strip()).title()

    if name == '':
        break

    student.append(name)

    first_note = float(input('1ª nota: '))
    student.append(first_note)

    second_note = float(input('2ª nota: '))
    student.append(second_note)

    average = (first_note + second_note) / 2
    student.append(average)

    if average >= 7:
        situation = 'Aprovado'
    elif average <5:
        situation = 'Reprovado'
    else:
        situation = 'Recuperação'
    student.append(situation)

    students_list.append(student[:])

    if len(students_list) == 1:
        print('Enter com valor vazio para finalizar!')

print(f'{"Nº":<4}{"Nome":<15}{"Média":>10}')
print(border)

for index, student in enumerate(students_list):

    print(f'{index+1:<4}{student[0]:<15}{student[3]:>10}')
print(border)

while True:

    answer = int(input('Consultar nota de qual aluno? ').strip())-1

    if answer == -1:
        break

    if answer <= len(students_list):

        print(border)
        print(
            f'A notas de {students_list[answer][0]} são {students_list[answer][1]} e {students_list[answer][2]}\n'
            f'Média: {students_list[answer][3]}\n'
            f'Situação: {students_list[answer][4]}')
        print(border)

    print('0 para finalizar!')
