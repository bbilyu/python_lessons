# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
#
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
#
# in
# -1
#
# out
# Negative value of the number of numbers!
# []
#
# in
# 10
#
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

import random


def removing_duplicate_elements(array: list):
    repetition_list = []
    for i in range((len(array))):
        if array.count(array[i]) > 1:
            repetition_list.append(array[i])
    for k in repetition_list:
        del array[array.index(k)]
    return array


while (True):
    n = int(input('Enter the length of the list: '))
    if n > 0:
        break
    elif n == 0:
        print("Please enter a value above zero")
        continue
    else:
        print("Negative value of the number of numbers! Please repeat input!")
        continue

list = [random.randint(0, 10) for x in range(n)]

print(list)
print(removing_duplicate_elements(list))
