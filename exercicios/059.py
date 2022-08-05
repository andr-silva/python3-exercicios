# Crie um programa que leia dois valores e mostre um menu:
#   [1] somar [2] subitrair [3] multiplicar [4] dividir [5] sair
# Seu programa deverá realizar a operação solicitada em cada caso.

option = 0

while option != 5 :

    print(f'[1] somar [2] subitrair [3] multiplicar [4] dividir [5] sair')

    option = (int(input('Escolha uma opção: ')))

    if option == 1:
        print('=-=-=- Somar -=-=-=')
        value_1 = int(input(f'Primeiro valor: '))
        value_2 = int(input(f'Segundo valor:  '))
        print(f'{value_1} - {value_2} = {value_1 - value_2}\n'
              '=-=-=-=-=-=-=-=-=-=')
    elif option == 2:
        print('=-=- Subtração -=-=')
        value_1 = int(input(f'Primeiro valor: '))
        value_2 = int(input(f'Segundo valor:  '))
        print(f'{value_1} - {value_2} = {value_1 - value_2}\n'
              '=-=-=-=-=-=-=-=-=-=')
    elif option == 3:
        print('=- Multiplicação -=')
        value_1 = int(input(f'Primeiro valor: '))
        value_2 = int(input(f'Segundo valor:  '))
        print(f'{value_1} x {value_2} = {value_1 * value_2}\n'
              '=-=-=-=-=-=-=-=-=-=')
    elif option == 4:
        print('=-=-= Divisão =-=-=')
        value_1 = int(input(f'Primeiro valor: '))
        value_2 = int(input(f'Segundo valor:  '))
        print(f'{value_1} ÷ {value_2} = {value_1 / value_2}\n'
              '=-=-=-=-=-=-=-=-=-=')
    elif option == 5:
        print('Finalizando.')
    else:
        option = int(input(
            '[1] Somar [2] Subtrair [3] Multiplicar [4] Dividir\n'
            'Opção inválida, escolha uma das opções acima: ')
        )
