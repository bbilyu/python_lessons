# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
#
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

import random

list = [random.randint(1, 100) for x in range(int(input('Enter the length of the list: ')))]


def sum_pairs_numbers(array: list):
    if len(array) % 2 == 0:
        list_tmp = [array[x] + array[- 1 - x] for x in range(int(len(array) / 2))]
    else:
        list_tmp = [array[x] + array[- 1 - x] for x in range(int(len(array) / 2))]
        list_tmp.append(array[int(len(array) / 2)])
    return list_tmp


print(list)
print(sum_pairs_numbers(list))
