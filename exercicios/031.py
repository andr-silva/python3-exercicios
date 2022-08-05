# Densenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200km e R$ para viagens mais longas.

km = float(input('Qual a distancia em Km? '))
value = km * 0.5 if km <= 200 else km * 0.45

print(f'O valor da viagem de {km:.0f}Km é de R${value:.2f}')
