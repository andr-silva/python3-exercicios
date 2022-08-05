# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 10 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

final_card = []
border = '-'*10

print(border, 'MEGA-SENA', border)

amount = int(input('Gerar quantos jogos?: ').strip())

for card in range(0, amount):

    numbers = []

    while True:

        number = randint(1, 60)

        if number not in numbers:
            numbers.append(number)
        if len(numbers) == 6:
            break

    numbers.sort()
    final_card.append(numbers[:])

for number, card in enumerate(final_card):

    print(f'{number+1}º Jogo ', ''.join(f'{position:^3} ' for position in card),)
