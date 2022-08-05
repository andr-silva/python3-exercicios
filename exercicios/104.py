# Crie um programa que tenha a função leiaInt(), qye vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação de aceitar apenas um valor númerico.

def number_int(msg):
    while True:
        value = input(msg,).strip()
        if value.isnumeric():
            return int(value)

        print('ERRO! Apenas números inteiros serão aceitos.')


number = number_int('Digite um número: ')
print(f'você digitou o número {number}')
