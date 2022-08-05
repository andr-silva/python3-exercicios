# Crie um programa que leia vários números interiso pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag).

count = sun_numbers = 0
number = int(input('Digite um numero [999 para parar] '))

while number != 999:

    sun_numbers += number
    count += 1
    number = int(input('Digite um numero [999 para parar] '))

print(f'Voce digitou {count} numeros e a soma entre eles é {sun_numbers} ')
