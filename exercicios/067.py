# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o númnero solicitado for negativo.

border = '-' * 13

while True:

    number = int(input('Quer ver a tabuada de qual valor? '))

    if number < 0:
        break

    print(border)    

    for value in range(1,11):
        result = number * value
        print(f' {number} x {value:2} = {result}')
    
    print(border)

    print('Digite um valor negativo para finalizar!')
