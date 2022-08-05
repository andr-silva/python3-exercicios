# Crie um programa onde o usuário posso digitar cinco valores numéricos e cadastre-os em uma lista, ja na posição correta de inserção (sem usar sort()). No final, mostre a lista ordenada na tela.

numbers = []

for add in range(0, 5):

    number = int(input('Digite um valor: '))

    if add == 0 or number > max(numbers):

        numbers.append(number)

        print(f'Adicionado no final da lista.')

    else:
        position = 0

        while position < len(numbers):

            if number <= numbers[position]:
                
                numbers.insert(position, number)

                print(f'Adicionado na posição {position} da lista')
                break

            position += 1

print(f'Os valores digitados foram : {numbers}')
