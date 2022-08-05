# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

city = str(input('Digite uma palavra: ')).strip()
checker = city[:5].upper() == 'SANTO'

print(checker)
