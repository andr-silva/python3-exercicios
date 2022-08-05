# Escreva um progama que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0.15 por Km rodado.

day = int(input('Quantos dias? '))
km = float(input('Quantos Km foram rodados: '))
daily = 60.00
km_driven = 0.15
total_payable = (km * km_driven) + (day * daily)

print(f'O total a pagar é de R${total_payable:.2f}.')
