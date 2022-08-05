# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#   Os 5 primeiros.
#   Os ultimos 4 colocados.
#   Times em ordem alfabética.
#   Em que posição está o time definido.

cblol_teams_22 = (
    'KaBuM!', 'FURIA', 'RED Canids', 'PaiN', 'Netshoes Miners',
    'Liberty', 'LOUD', 'Rensga', 'Flamengo', 'INTZ'
)
border = f'\n\n {"-" * 80}\n\n'


print('lista de times do CBLOL:\n')

for teams in cblol_teams_22[0:]:
    position = (cblol_teams_22.index(teams)) + 1

    print(f'{teams}', end='')
    print("." if position == len(cblol_teams_22) else ", ", end='')

print(f'{border}Os 3 primeiros são:')

for teams in cblol_teams_22[0:3]:
    position = (cblol_teams_22.index(teams)) + 1

    print(f'{position}º {teams}', end='')
    print("." if position == 3 else ", ", end='')

print(f'{border}Os 2 últimos  são: ')

for teams in cblol_teams_22[-2:]:
    position = (cblol_teams_22.index(teams)) + 1

    print(f'{position}º {teams}', end='')
    print("." if position == 10 else ", ", end='')

print(f'{border}Em ordem alfabetica: ')

for teams in sorted(cblol_teams_22[0:]):
    position = (sorted(cblol_teams_22[0:]).index(teams)) + 1

    print(f'{teams}', end='')
    print("." if position == 10 else ", ", end='')

wanted_team = 'PaiN'
position_team = cblol_teams_22.index(wanted_team) + 1

print(f'{border}{wanted_team} está na {position_team}ª posição\n')
