# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gold feitos em cada partida. No final, tudo isso ficará guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

player = {'Nome': str(input('Nome do jogador: ')).title().strip()}
towers = []
total_towers = 0
border = '-' * 70

while True:
    tower = input('Número de torres: ').strip()
    if tower == '':
        break
    else:
        tower = int(tower)
        towers.append(tower)
        total_towers += tower
    if len(towers) == 1:
        print('Enter com valor vazio para finalizar!')

player['Torres'] = towers
player['Total'] = total_towers

print(
    f'{border}\n'
    f'{player}\n'
    f'{border}'
)

for key, value in player.items():
    print(f'{key}: {value}')

print(
    f'{border}\n'
    f'{player["Nome"]} Jogou {len(player["Torres"])} partidas.'
)

for position, value in enumerate(player["Torres"]):

    if value == 0:
        pl = f'nenhuma torre derrubada'
    elif value == 1:
        pl = f'{value} torre derrubada'
    else:
        pl = f'{value} torres derrubadas'

    print(f'- {position+1}ª partida {pl}.')
