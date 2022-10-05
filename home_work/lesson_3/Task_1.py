# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import sample


def create_random_list(count: int):
    if count < 0:
        return "Negative value of the number of numbers!"
    return sample(range(1, count * 2), count)


def sum_elements_odd_positions(list_with_numbers: list):
    i = 0
    sum = 0
    while i <= len(list_with_numbers) - 1:
        sum += list_with_numbers[i]
        i += 2
    return sum


list = create_random_list(int(input(f'Enter the length of the list: ')))

print(list)
print(sum_elements_odd_positions(list))
