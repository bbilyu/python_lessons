# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
#
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
#
# in
# 10
#
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

list_input = list(map(int,input('Вводите целые числа через пробел: ').split()))
print(list_input)
print([i for i in list_input if list_input.index(i) != 0 and list_input[list_input.index(i)-1] < i])