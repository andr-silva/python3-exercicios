# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5¢ de desconto.

value = float(input('Qual o valor do produto: R$'))
discount = value - (value * 5 / 100)
economy = value - discount

print(f'O produto que custava R${value:.2f}, na promoção com desconto de 5% vai custar R${discount:.2f}, economizando R${economy:.2f}.')
