# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

num = float(input('Digite um numero: '))
result = trunc(num)

print(f'o valor digitado foi {num} e sua porção inteira é {result}.')
