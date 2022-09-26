# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random

def shuffle_list(array: list):
    for x in range(num):
        rnd_pos = random.randint(0, num - 1)
        tmp = array[x]
        array[x] = array[rnd_pos]
        array[rnd_pos] = tmp

num = int(input('Enter a number: '))
list = [x for x in range(num)]

print(list)

shuffle_list(list)

print(list)
