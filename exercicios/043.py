# Desenvolva um lógia que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com os dados.py abaixo:
#   Abaixo de 18.5: Abaixo do Peso
#   Entre 18.5 e 25: Peso ideal
#   25 até 30: Sobrepeso
#   30 até 40: Obesidade
#   Acima de 40: Obesidade mórbida

weigth = float(input('Qual o seu peso? (Kg) '))
heitgh = float(input('Qual é sua altura? (cm) '))
imc = weigth / ((heitgh/100) ** 2)

if imc < 18.5:
    result = 'abaixo do peso'
elif imc <= 25:
    result = 'no peso ideal'
elif imc <= 30:
    result = 'com sobrepeso'
elif imc <= 30:
    result = 'com obesidade'
else:
    result = 'com obesidade mórbida'

print(f'O IMC é de {imc:.2f} e está {result}!')