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
