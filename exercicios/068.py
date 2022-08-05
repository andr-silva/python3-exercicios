# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

from random import randint

win = 0
talks = ['', 'Revanche! ', 'Estava só aquecendo. ', 'Bora a ultima, sério! ']

print(f'Vamos jogar PAR ou ÍMPAR')

while True:

    computer = randint(0, 10)
    player = 11

    while player not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:

        player = int(input(f'{(talks[win])}Digite um valor: '))
        break

    total = computer + player
    choic = ' '

    while choic not in 'PI':

        choic = str(input('[I] Ímpar [P] Par: ')).strip().upper()[0]

    if choic == "P":

        if total % 2 == 0:
            result = 'PAR'
            win += 1
        else:
            result = 'ÍMPAR'
            break

    elif choic == "I":

        if total % 2 == 1:
            result = 'PAR'
            win += 1
        else:
            result = 'PAR'
            break

    elif win == 4:
        break

print(f'Você jogou {player} e eu {computer} que soma {total} que é {result}')

if win == 0:
    print(f'Venci de primeira. hihihi')

elif win == 1:
    print(f'Empatamos, você ganhou 1 vez e eu tambem')

elif win > 2:
    print(f'Você venceu {win} vezes.')

elif win == 4:
    print(f'Eu me rendo, você venceu {win} vezes.')
