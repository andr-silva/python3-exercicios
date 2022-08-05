from moeda import half, decrease, currency

price = float(input('Digite o preço: '))

print(
    f'A metade de {currency(price)} é {currency(half(price))}\n'
    f'Reduzindo 25% de {currency(price)} temos {currency(decrease(price, 25))}'
)
