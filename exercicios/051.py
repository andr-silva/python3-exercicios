# Desenvolva um programa que leio o primeiro termo e a razão de uma PA.
#No final mostre os 10 primeiros termos dessa prograssão.

first_term = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
tenth_term = 10 * reason

for progression in range(first_term, tenth_term+1, reason):

    print(f'{progression}', end=' ')


# Outra forma
print()
for tenth_term in range(0, 10,):
    print(f'{first_term + reason * tenth_term}', end=' ')
