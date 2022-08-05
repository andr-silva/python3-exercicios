# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com aumento de 15%.

salary = float(input('Qual o salário do funcionario: R$'))
new_salary = salary+(salary*15/100)
readjustment = new_salary - salary

print(
    f'O salário de R${salary:.2f} com o reajuste de 15% será de R${new_salary:.2f}\n'
    f'O reajuste foi de R${readjustment:.2f}'
)
    