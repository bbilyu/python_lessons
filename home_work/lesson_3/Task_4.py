# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
#
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

import random

list = [round(random.uniform(1, 10), 2) for x in range(int(input('Enter the length of the list: ')))]
print(list)


def find_difference(array: list):
    min = max = round(array[0] % 1, 2)
    for x in range(len(array)):
        if array[x] % 1 < min:
            min = round(array[x] % 1, 2)
        if array[x] % 1 > max:
            max = round(array[x] % 1, 2)
    print(f"Min: {min}, Max: {max}. Difference: {round(max - min, 2)}")


find_difference(list)
