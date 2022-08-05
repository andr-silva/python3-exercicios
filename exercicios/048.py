# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('Farei a soma em numeros divisiveis por 3')

select = (int(input('Digite um numero: ')))
couter = 0
addition = 0

for number in range(1, select+1, 2):
    if number % 3 == 0:
        couter += 1
        addition += number
        
print(f'A soma de todos os {couter} os valores  é {addition}')
