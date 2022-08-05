# Faça um programa que leia uma frase e mostre:
#   Quantas vezes apare a letra "A".
#   Em que posição ela aparece a primeira vez.
#   Em que posição ela aparece a última vez.

phrase = str(input('Digite uma frase: ')).strip().upper()
letter_counter = phrase.count("A")
first_letter_position = phrase.find("A") + 1
last_letter_position = phrase.rfind("A") + 1

print(
    f'A letra A aparece {letter_counter} vezes na frase.\n'
    f'A letra A aparece na {first_letter_position}ª letra.\n'
    f'A última letra A apareceu na {last_letter_position}ª letra.'
)
