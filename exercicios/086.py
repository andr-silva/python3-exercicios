# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela com a formatação correta

matriz = [[],[],[]]
width = []

for lin in range(0, 3):

    for col in range(0, 3):
        value = int(input(f"Digite um valor para [{lin+1},{col+1}]: "))
        matriz[lin].append(value)
        width.append(value)

max_width = len(str(max(width)))+2
border = "═"*(max_width)
border_top = f'╔{border}╦{border}╦{border}╗'
border_mid = f'╠{border}╬{border}╬{border}╣'
border_bot = f'╚{border}╩{border}╩{border}╝'

for lin in range(0, 3):

    if lin == 0:
        print(border_top)
    else:
        print(border_mid)

    for col in range(0, 3):
   
        print(f'║{matriz[lin][col]:^{max_width}}', end='')

    print('║')

print(border_bot)
