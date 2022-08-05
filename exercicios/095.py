# Aprimore o exercício 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes co aproveitamento de cada jogador.

player = {}
players = []
towers = []
border = '-' * 50
while True:

    if len(players) == 1:
        print('Enter vazio para finalizar!')

    name = input('Nome do jogador: ').title().strip()

    if name == '':
        break

    print(f'{name} resgistado!')

    total_towers = 0

    while True:

        tower = input(f'Número de torres na {len(towers)+1}ª partida: ').strip()

        if tower == '':
            print(f'{total_towers} torres registado para {name}.')
            break

        tower = int(tower)
        total_towers += tower

        towers.append(tower)

    player['Nome'] = name
    player['Torres'] = towers[:]
    player['Total'] = total_towers

    players.append(player.copy())
    towers.clear()
    player.clear()

print(
    f'{border}\n'
    'cód ', end=''
)

for index in player.keys():
    print(f'{index:<20}', end='')

print(f'\n{border}')

for position, data in enumerate(players):

    print(f'{position:>3} ', end='')

    for value in data.values():

        print(f'{str(value):<20}', end='')

    print()

print(border)

while True:

    search = input('Mostrar detalhes de qual jogador? ')

    if search == '':
        print('Finalizando consulta...')
        break

    search = int(search)

    if search >= len(players):
        print('Código inválido.')

    else:
        print(
            f'{border}\n'
            f'Histórico do jogador {players[search]["Nome"]}:'
        )

        for match, tower in enumerate(players[search]['Torres']):
            if tower == 0:
                tower = 'nenhuma'
                pl = ''
            elif tower == 1:
                pl = ''
            else:
                pl = 's'

            print(f'    {match+1}ª partida {tower} torre{pl} derrubada{pl}.')

        print(border)
