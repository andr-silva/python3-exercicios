# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a congição de parada. No final, mostre quantos números foram digitados e qual o a soma entre eles (desconsiderando o flag).

sun_numbers = count = 0

while True:

    number = int(input('Digite um numero inteiro [999 para parar]: '))

    if number == 999:
        break
    
    print(f'Número {number} armazenado!')
    count += 1
    sun_numbers += number

print(f'Foram digitados {count} números e a soma entre eles é {sun_numbers}')
