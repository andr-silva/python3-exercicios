# Faça um progrma que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e menor valor aigitado e as suas respectivas posições na lista.

numbers = []

for number in range(0, 5):
    numbers.append(float(input('Digite um número: ')))

print(
    f'Os valores digitados foram:\n{numbers}\n'
    f'O maior valor da lista é {max(numbers)} na posição ', end=''
)

# forma 1
for index, number in enumerate(numbers):
    if number == max(numbers):
        print(index, end=' ')
        
# forma 2
print(
    f'\nO menor valor da lista {min(numbers)} na posição',
    "".join(f'{index} ' for index, number in enumerate(numbers) if number == min(numbers))
)
