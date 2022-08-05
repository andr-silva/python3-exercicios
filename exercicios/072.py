# Crie um programa que tenha uma tupla totalmente preenchida com a contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

number_list = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco','seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze','treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
    'dezenove', 'vinte'
)

while True:

    while True:

        number = int(input('Digite um número entre 0 e 20: '))

        if 0 <= number <= 20:
            break

        print('Número inválido, tente novamente.')

    print(f'Voce digitou o número {number_list[number]}.')

    cont = str(input('Finalizar operação? [S] [N] ')).strip().upper()
    
    if cont not in 'N':
        print('Operação finalizada.')    
        break
