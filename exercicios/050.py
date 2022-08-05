# Desenvolva um programa que leia 'seis números inteiros' e mostre a soma daqueles que foram pares, Se o valor digitado for Ímpar, desconsidere-o.

counter = 0
addition = 0

for position in range(1, 7,):

    selected = int(input(f'Digite o {position}º numero: '))

    if selected % 2 == 0:
        counter += 1
        addition += selected

print(f'Você informou {counter} numeros pares e a soma foi {addition}')
