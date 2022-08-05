# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, incerindo o nome deles e escrevendo o nome do escolhido.

from random import choice

student_1 = str(input('Primeiro aluno: '))
student_2 = str(input('Segundo aluno: '))
student_3 = str(input('Terceiro aluno: '))
student_4 = str(input('Quarto aluno: '))

list_of_students = [student_1, student_2, student_3, student_4]

print(f'O aluno escolhido foi {choice(list_of_students)}')
