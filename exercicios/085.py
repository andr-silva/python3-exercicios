# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista unpica que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numbers = [[], []]

while True:

    number = input('Digite um número: ').strip()
    if number == '':
        break

    number = int(number)

    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)
    if len(numbers[0]) == 0 or len(numbers[1]) == 0:
        
        print('Enter com valor vazio para finalizar!')

numbers[0].sort()
numbers[1].sort()

print(
    f'Todos os números: {numbers}\n'
    f'Números ímpares: {numbers[1]}\n'
    f'Numeros pares: {numbers[0]}'
)
