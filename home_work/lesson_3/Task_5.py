# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5


def nega_fibo(number: int):
    list = []
    fib1 = fib1_2 = fib2_2 = 1
    fib2 = -1
    if number == 0:
        return [0]
    if number == 1:
        return [fib1, 0, fib1_2]
    if number == 2:
        return [fib2, fib1, 0, fib1_2, fib2_2]
    list.extend([fib2, fib1, 0, fib1_2, fib2_2])
    for i in range(2, number):
        fib1, fib2 = fib2, fib1 - fib2
        fib1_2, fib2_2 = fib2_2, fib1_2 + fib2_2
        list.insert(0, fib2)
        list.append(fib2_2)
    return list


print(*nega_fibo(int(input('Enter number: '))))
