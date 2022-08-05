from moeda import *

price = float(input('Digite o preço: '))

print(
    f'A metade de {price} é R${half(price)}\n'
    f'Reduzindo 25% de R${price}, temos R${decrease(price, 25)}'
)
