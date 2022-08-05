def increase(value, rate, sign=False):
    result = value + (value * rate/100)
    return result if sign is False else currency(result)


def decrease(value, rate, sign=False):
    result = value - (value * rate/100)
    return result if sign is False else currency(result)

def double(value,sign=False):
    result = value * 2
    return result if sign is False else currency(result)


def half(value,sign=False):
    result = value / 2
    return result if sign is False else currency(result)


def currency(value, sign='R$'):
    return f'{sign}{value:.2f}'.replace('.',',')


def summary(value=0,rate=10):
    border = '-'*30
    print(
        f'{border}\n'
        f'{"Resumo do valor".center(30)}\n'
        f'{currency(value).center(30)}\n\n'
        f'Dobro do preço: {double(value, True)}\n'
        f'Metade do preço: {half(value, True)}\n'
        f'Acrescentando {rate}%: {increase(value, rate, True)}\n'
        f'Reduzindo {rate}%: {decrease(value, rate, True)}\n'        
        f'{border}'
    )
