# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

phrase = str(input('Digite a frase: ')).strip().upper()
words = phrase.split()
join_words = ''.join(words)
inverse = ''

for char in range(len(join_words) - 1, -1, -1):
    inverse += join_words[char]

if inverse == join_words:
    result = 'Temos um palíndromo!'
else:
    result = 'A frase digitada não é um palíndromo!'

print(
    f'O inverso de {join_words} é {inverse}.\n'
    f'{result}'
)
