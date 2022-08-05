# Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros.

value = float(input('Digite uma distância em metros: '))
cm = value*100
mm = value*1000

print(f'A medida de {value}m corresponde a {cm:.0f}cm e {mm:.0f}mm.')
