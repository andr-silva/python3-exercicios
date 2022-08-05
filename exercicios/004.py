# Desenvolva um programa que leia algo e mostre o seu tipo primitivo e todas as informações possiveis entre ele.

value = input('Digite algo: ')

print(f'O tipo primitivo de {value} é {type(value)}')
print(f'Só tem espaço? {value.isspace()}')
print(f'É númerico? {value.isnumeric()}')
print(f'É alfabético? {value.isalpha()}')
print(f'É alfanumérico? {value.isalnum()}')
print(f'Está maiúsculo? {value.isupper()}')
print(f'Está em minúsculo? {value.islower()}')
print(f'Está captalizada? {value.istitle()}')
