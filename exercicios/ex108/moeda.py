def increase(value,rate):
    result = value + (value * rate/100)
    return result


def decrease(value, rate):
    result = value - (value * rate/100)
    return result


def double(value):
    result = value * 2
    return result


def half(value):
    result = value / 2
    return result


def currency(value, sign='R$'):
    return f'{sign}{value:.2f}'.replace('.',',')
