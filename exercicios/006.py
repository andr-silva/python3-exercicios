# Desenvolva um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número inteiro: '))
double = num * 2
triple = num * 3
root = pow(num, (1/2))

print(
    f'O dobro de {num} é igual a {double}.\n'
    f'O triplo de {num} é igual a {triple}.\n'
    f'A raiz quadrada de {num} é igual a {root:.2f}'
)
