# faça um programa que tenha uma função chamada escreva(), que receba um texto qualuqer como parâmetro e mostre uma mensagem com tamanho adaptável.

def adapted_edge():

    value = str(input('Digite algo: '))
    width = 2 + len(value)
    border = (type_edge())*width

    print(
        f'{border}\n'
        f'{value:^{width}}\n'
        f'{border}'
    )


def type_edge():

    types = ['-','ˍ','―', '┈', '═', '╍', '╼','≡','☰','☷',]

    print()

    for symbol in range(0,5):
        print(f'[{symbol}] {types[symbol]*10} [{symbol+5}] {types[symbol+5]*10}')
    
    print()

    selection = int(input('Formato da borda: '))

    return types[selection]


adapted_edge()
