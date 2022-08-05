# Crie um programa onde o usuário digite uma expressão qualuqer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com parentêses abertos e fechados na ordem correta.

expression = str(input('Digite a expressao: '))
stack = []
result = 'Expressão inválida!'

for symbol in expression:
    if symbol == '(':
        stack.append('(')
    elif symbol == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break

if len(stack) == 0:
    result = 'Expressão válida!'

print(result)

# outra maneira
p_open = expression.count('(')
p_closed = expression.count(')')

if expression.index(')') > expression.index('('):

    if p_open == p_closed:
        result = 'Expressão válida!'
else:
    result = 'Expressão inválida!'

print(result)