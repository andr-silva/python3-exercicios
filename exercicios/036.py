# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

house_value = float(input('Qual o valor da casa: R$'))
salary = float(input('Qual o sua renda mensal: '))
age = int(input('Quantos anos de financiamento? '))
payment = house_value/(age * 12)

if payment <= salary * 0.3:
    print(
        f'Financiamento aprovado!\n'
        f'A menslidade será de R${payment:.2f}'
    )
else:
    print(f'Emprestimo recusado')
    