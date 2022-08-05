# refaça o exercício, mostrando a tabuada de um número que o usuário escolher, sṕ qie aora ultilizando um 'laço for'.

number = int(input('Digite um número para ver a tabuada: '))
border = '=-' * 7

print(border)

for value in range(1, 11):
    result = number * value
    print(f'{number}  x {value:2}  = {result}')

print(border)
