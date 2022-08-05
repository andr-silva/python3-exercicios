# Crie um programa que leia vários npumeros inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor informado. O prodgrama deve perguntar ao usuário se ele quer ou não continuar a digitaar valores.

answer = 'S'
sum_numbers = count = mean = larger = smaller =0

while answer in 'sS':

    number = float(input('Digite um numero: '))
    sum_numbers += number
    count += 1

    if count == 1:
        larger = smaller = number
    else:
        if number > larger:
            larger = number
        if number < smaller:
            smaller = number

    answer = str(input('Quer continuar? [S] [N] : ')).upper().strip()[0]

    if answer not in ['S', 'N']:
        answer = str(input(
            'Digito inválido, tente novamente.\n'
            '[S] Para SIM [N] Para NÃO : ')
        ).upper().strip()[0]

mean = sum_numbers / count

print(
    f'Voce digitou {count} números e a media entre eles é {mean:.2f}\n'
    f'O menor valor é {smaller} e o maior é {larger}'
)
