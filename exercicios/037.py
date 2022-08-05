# Escreva um programa que leia um número inteiro quelquer e peça para o usuário escolher qual será a case de conversão:
#   1 para binário
#   2 para octal
#   3 para hexadecimal

number = int(input('Digite um numero inteiro: '))

print(
    'escolha  uma das bases de conversão:\n'
    '[1] converter para BINÁRIO\n'
    '[2] converter para OCTAL\n'
    '[3] converter para HEXADECIMAL'
)

selection = int(input('Sua opção: '))

if selection == 1:
    print(f'{number} convertido para BINÁRIO é igual a {number:b}')
elif selection == 2:
    print(f'{number} convertido para OCTAL é igual a {number:o}')
elif selection == 3:
    print(f'{number} convertido para HEXADECIMAL é igual a {number:x}')
else:
    print('Opção inválida. Tente novamente')
