# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as vogais.

words = ('aprender', 'elogiar', 'aluno', 'programar', 'trabalho', 'praticar', 'entender', 'compartilhar', 'ensinar')

for word in words:

    print(f'Na palavra {word} temos ', end='')

    for lyrics in word:
        if lyrics.lower() in 'aeiou':
            print(lyrics.upper(), end=' ')

    print(end='\n')
