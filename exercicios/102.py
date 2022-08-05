# Crie um programa que tenha uma função fatorail() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opicional) indicando se será mostrado ou nçao na tela o processo de cálculo e fatorial.

def factorial(value, show=False):
    """
    - Calcula o Fatorial de um número.
    :param value: o número a ser calculado.
    :param show:(opcional) Mostra ou não a conta.
    :return: O valor do Fatorial do número informado.
    """
    result = 1

    for count in range(value, 0, -1):

        if show:
            symbol = 'x ' if count > 1 else '= '
            print(count, symbol, end='')

        result *= count

    return result


number = int(input('Digite um número inteiro: '))

print(factorial(number, show=True))
