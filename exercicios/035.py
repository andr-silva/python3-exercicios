# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

seg_1 = float(input('Primeiro segmento: '))
seg_2 = float(input('Segundo segmento: '))
seg_3 = float(input('terceiro segmento: '))

if seg_1 < seg_2 + seg_3 and seg_2 < seg_1 + seg_3 and seg_3 < seg_1 + seg_2:
    verification = 'formam'
else:
    verification = 'não formam'

print(f'Os segmentos informados {verification} um triângulo!')
