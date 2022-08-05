# Refaça o exercicío 035 com triângulos, acrescentando o recurso de mostrar que  tipo de triângulo será formado:
#   Equilátero: todos os lados iguais
#   ISósceles: dois lados iguais
#   Todos lados diferentes

seg_1 = float(input('Primeiro segmento: '))
seg_2 = float(input('Segundo segmento: '))
seg_3 = float(input('terceiro segmento: '))
type = does_not_form = ''

if seg_1 < seg_2 + seg_3 and seg_2 < seg_1 + seg_3 and seg_3 < seg_1 + seg_2:
    if seg_1 == seg_2 == seg_3:
        type = ' EQUILÁTERO'
    elif seg_1 != seg_2 != seg_3 != seg_1:
        type = ' ESCALENO'
    else:
        type = ' ISÓSCELES'
else:
    does_not_form ='NÃO'

print(f'Os segmentos informados {does_not_form} formam um triângulo{type}!')
