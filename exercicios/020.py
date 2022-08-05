# O mesmo professor do exercico anterior (019) quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

student_1 = str(input('Primeiro aluno: '))
student_2 = str(input('Segundo aluno: '))
student_3 = str(input('Terceiro aluno: '))
student_4 = str(input('Quarto aluno: '))

list_of_students = [student_1, student_2, student_3, student_4]

shuffle(list_of_students)

print(
    f'A ordem de apresentação será:\n'
    f'{list_of_students}'
)
