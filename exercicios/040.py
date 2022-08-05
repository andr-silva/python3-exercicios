# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#   Média abaixo de 5.0: REPROVADO
#   Média entre 5.0 e 6.9: RECUPERAÇÃO
#   Média 7.0 ou superior: APROVADO

note_1 = float(input('Qual a primeira nota: '))
note_2 = float(input('Qual a segunda nota: '))
note_3 = float(input('Qual a terceira nota: '))

average =  (note_1 + note_2 + note_3) / 3
phrase_for_average = f'Sua média foi {average:.2f},'
value_for_approval = 7
value_for_disapproval = 5

if average < 0 :
    print('Valores digitados inválidos, verifique e tente novamente.')
elif average >= value_for_approval:
    print(phrase_for_average,'aprovado!')
elif average < value_for_disapproval:
    print(phrase_for_average,'reprovado!')
else:
    print(phrase_for_average,'recuperação')
