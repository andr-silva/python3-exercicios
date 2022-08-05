# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 r peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

border = '-=-'*10

print(
    f'{border}\n'
    'Escolha um número entre 0 e 5\n'
    f'{border}\n'
)

chosen_number = randint(0, 5)
typed_number = int(input('Qual  número escolhi? '))

if chosen_number == typed_number:
    print('Você acertou!')
else:
    print(f'Você errou! Era o número {chosen_number}')
