# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior núnero,

from random import randint
from time import sleep
from operator import itemgetter

players = {}
ranking = {}
tiebreaker = {}
border = '-' * 20
number = int(input('Número de jogadores: '))
dice = int(input('Dado de quantos lados? '))

for play in range(0, number):
    name = str(input(f'{play+1}º jogador: ')).title().strip()
    print(f'{name} rolou o dado.')
    players[f'{name}'] = randint(1, dice)

print(border)

for name, number in players.items():
    sleep(1)
    print(f'{name:<5} - {number:3}.')

print(border)

ranking = sorted(players.items(), key=itemgetter(1), reverse=True)

if ranking[0][1] == ranking[1][1]:

    print(f'Desempate entre ', end='')

    for name, number in ranking:

        if number == ranking[0][1]:
            print(name, end=' ')
            tiebreaker[name] = randint(1, dice)

    print('\n', border)

    for name, number in tiebreaker.items():
        sleep(4)
        print(f'{name:<5} - {number:3}')

else:
    sleep(1)
    print(
        f'{ranking[0][0]} ganhou!\n'
        f'{border}')

    for name, number in ranking:
        print(f'{name:<5}  {number:3}')

print(border)
