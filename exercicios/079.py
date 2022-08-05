# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número ja existaa lá dentro, ele não será adionado. No final, serão exibidos totos os valores únicos digitados, em ordem crescente.

numbers = []

while True:
    number = (int(input("digite um numero: ")))

    if number not in numbers:

        numbers.append(number)

        print(f'Valor {number} adiocionado.')

    else:
        
        print(f'O valor {number} ja foi adiocionado à lista.')

    answer = str(input('Adicionar outro valore? [S] [N] ')).upper()

    if answer in 'N':
        break

numbers.sort()

print(f'Os valores na lista são: {numbers}')
