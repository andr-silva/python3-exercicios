# Faça um progtama que tenha uma função de chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analizar todos os valores e dizer qual deles é o maior.

def higher_number(*value):
    higher = 0
    for number in value:
        if number > higher:
            higher = number
    print(higher)

higher_number(3, 2, 7, 9, 4, 1)
