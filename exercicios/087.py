# Aprimore o exercicio anterior, mostrando no final:
#   A soma de todos os valores pares digitados.
#   A soma dos valores da terceira coluna.
#   O maior valor da segunda linha.

# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela com a formatação correta

matriz = [[],[],[]]
width = []
sum_even = third_column = second_line_value = 0

for lin in range(0, 3):

    for col in range(0, 3):
        value = int(input(f"Digite o valor para [{lin+1},{col+1}]: "))
        matriz[lin].append(value)
        width.append(value)

max_width = len(str(max(width)))+2
border = "═"*(max_width)
border_top = f'╔{border}╦{border}╦{border}╗'
border_mid = f'╠{border}╬{border}╬{border}╣'
border_bot = f'╚{border}╩{border}╩{border}╝'

print()

for line in range(0, 3):

    if line == 0:
        print(border_top)
    else:
        print(border_mid)

    for col in range(0, 3):
   
        print(f'║{matriz[line][col]:^{max_width}}', end='')
        if matriz[line][col] % 2 == 0:
            sum_even += matriz[line][col]

    print('║')

print(border_bot)

for value in range(0,3):

    third_column += matriz[value][2]

    if value == 0 or matriz[1][value] > second_line_value:
        second_line_value = matriz[1][value]

print(f'\nA soma dos valores pares é: {sum_even}')
print(f'A soma dos valores da 3ª coluna é: {third_column}\n'
      f'O maior valor da 2ª coluna é: {second_line_value}')
