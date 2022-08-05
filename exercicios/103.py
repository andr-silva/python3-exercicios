# Faça um programa que tenha uma função chama ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def player_registration(name_player='', value=''):

    plural = ''

    if name_player == '':
        player = 'não informado'
    else:
        player = name_player
    
    if value == '' or value == '0':
        value = 'nenhuma'
    elif value == '1':
        plural = ''
    else:
        plural = 's'


    print(f'Jogador(a) {player} derrubou {value} torre{plural}.')


name = input('Nome: ')
number = input('Torres derrubadas: ')

player_registration(name, number)
