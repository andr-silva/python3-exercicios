# Melhore o jogo do exercício 028 onde o computador vai "pensar" em um npumero entre 0 e 10. Só que agora o jogodor vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

border = '---'*10
choice = randint(0, 10)
lives = 4

print(f'{border}\nEscolha um número entre 0 e 10\n{border}')

typed = int(input('Qual é o seu palpite? '))


while choice != typed and lives != 1:
    if lives == 2:
        plural = ['', '']
    else:
        plural = ['m', "s"]

    if choice > typed:
        lives -= 1
        typed = int(input(f'Mais... Resta{plural[0]} {lives} tentativa{plural[1]}: '))
    elif choice < typed:
        lives -= 1
        typed = int(input(f'Menos... Resta{plural[0]} {lives} tentativa{plural[1]}: '))

if choice == typed:
    print('Você Ganhou!')
else:
    print(f'Você Perdeu! Era o número {choice}')
