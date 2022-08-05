# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digítos separados.
# Ex:
#   Digite um numero: 1834
#   unidade: 4, dezena: 3, centena: 8, milhar: 1

number = int(input('Digite um número com 4 dígitos: '))
unity = number // 1 % 10
dozens = number // 10% 10
hundreds = number // 100 % 10
thousands = number // 1000 % 10

print(
    f'Analisando o numero {number}\n'
    f'Unidade: {unity}\n'
    f'Dezena:  {dozens}\n'
    f'Centena: {hundreds}\n'
    f'Milhar:  {thousands}'
)
