# Crie um programa que leia quanto dinheiro a pessoa tem e mostre quantos dólares é possivel comprar.

real_value = float(input('Quantos reais será convertidos? R$ '))
dollar_value = float(5.35)
calculation = real_value / dollar_value

print(
    f'1 real é igual a {dollar_value} dólar americano.\n'
    f'É possivel comprar ${calculation:.2f}.'
)
