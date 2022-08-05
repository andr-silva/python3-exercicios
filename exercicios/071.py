# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão intregues.

border = '-' * 25

print(f'{border}\n--  Banco Santo André  --\n{border}')

while True:

    value = int(input(
        'Cédulas disponíveis\n'
        'R$100 R$50 R$10 R$5\n\n'
        'Valor do saque: R$ ')
        )

    if value % 5 == 0:
        break
    else:
        print(f'Valor inválido!\n{border}')

total = value
bank_note = 100
total_bank_note = 0

while True:

    if total >= bank_note:
        total -= bank_note
        total_bank_note += 1
    else:
        if total_bank_note > 0:

            if total_bank_note > 1:
                pl = 's'
            else:
                pl = ''

            print(f'{total_bank_note} cédula{pl} de R${bank_note}')

        if bank_note == 100:
            bank_note = 50
        elif bank_note == 50:
            bank_note = 20
        elif bank_note == 20:
            bank_note = 10
        elif bank_note == 10:
            bank_note = 5

        total_bank_note = 0

        if total == 0:
            break

print(border)