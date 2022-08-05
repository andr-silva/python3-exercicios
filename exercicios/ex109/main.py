from moeda import half, decrease, currency

price = float(input('Digite o preço: '))

print(
    f'A metade de {currency(price)} é {half(price,True)}\n'
    f'Reduzindo 25% de {currency(price)} temos {decrease(price, 25,True)}'
)
