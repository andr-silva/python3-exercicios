# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Pasa salários superiores a R$ 1.2550,00, calcule um aumento de 10%.
# Para salário inferiores ou iguais, o aumento é de 15%.

from decimal import Decimal

salary = Decimal(str(input('Qual o salario do funcionário: R$').replace(',', '.')))

if salary <= 1250:
    new_salary = round(salary * Decimal(1.15), 2)
elif 2500 <= salary < 3750:
    new_salary = round(salary * Decimal(1.10), 2)
else:
    new_salary = round(salary * Decimal(1.075), 2)

addition = new_salary - salary

print(f'O aumento será de R${addition} atualizando para R${new_salary}')
