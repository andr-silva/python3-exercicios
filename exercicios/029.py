# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizrndo que ele foi multado.
# A multa vai custar R$7.00 por cada km acima do limite.

velocity = float(input('Qual a velocidade do carro? '))
fine_amount = (velocity-80)*7

if velocity <= 80:
    print('Boa Viagem')
else:
    print(
        'VOCÊ EXCEDEU O LIMITE PERMITIDO DE 80Km/h!\n'
        f'MULTADO EM R${fine_amount:.2f}'
    )
