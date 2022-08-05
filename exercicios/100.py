# Faça um programa que tenha uma lista chama números e duas funções chama sorteia() e SomaPar(). A primeia função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint

def draw_numbers(higher_number, smallest_number, number_of_times):

    list_numbers = []

    for number in range(number_of_times):
        list_numbers.append(randint(higher_number, smallest_number))

    return list_numbers


def even_sum(value):

    sum_list = 0

    for number in value:

        if number % 2 == 0:
            sum_list += number

    return sum_list


def odd_sum(value):

    sum_list = 0

    for number in value:

        if number % 2 == 1:
            sum_list += number

    return sum_list


numbers = draw_numbers(1, 10, 5)

print(numbers)
print(even_sum(numbers))
print(odd_sum(numbers))
print(sum(numbers))
