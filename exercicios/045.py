# Crie um programa que faça o computador jogar Jokenpô com você.


from random import randint
from time import sleep
from emoji import emojize

options =  ['Pedra :rock:', 'Papel :roll_of_paper:', 'Tesoura :scissors:']
computer = randint(0, 2)

print(
    'Escolha sua opção:',
    emojize(f'[1] {options[0]}    [2] {options[1]}   [3] {options[2]}')
)

player = (int((input('Qual é sua jogada? ')))-1)

print('\n  JO')
sleep(0.5)
print('    KEN')
sleep(0.5)
print('       PÔ\n')
sleep(0.5)

print(emojize(f'Computador:{options[computer]}\nVocê: {options[player]}\n'))

won = 'Você ganhou!'
lose = 'Você perdeu!'
invalid = 'Jogada inválida'
result = 'Empate'

if computer == 0:
    if player == 1:
        result = won
    elif player == 2:
        result = lose

elif computer == 1:
    if player == 2:
        result = won
    elif player == 0:
        result = lose

elif computer == 2:
    if player == 0:
        result = won
    elif player == 1:
        result = lose
else:
    result = invalid
    

print(result)
