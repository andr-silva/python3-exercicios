# Escreva um programa que converta a temperatura informada em ºC e converta em ºF. 

c = float(input('Qual a temperatura em ºC: '))
f = ((9 * c)/5 + 32)
k = c + 273.15

print(
    f'A temperatura de {c}ºC corresponde a {f}ºF.\n'
    f'E também corresponde a {k}K'
)
