# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
#
# in
# 54
# out
# [2, 3, 3, 3]
#
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
#
# in
# 650
# out
# [2, 5, 5, 13]

def prime_factors(number: int):
    list = []
    i = 2
    while i * i <= number:
        if number % i == 0:
            list.append(i)
            number //= i
        else:
            i += 1
    if number > 1:
        list.append(number)
    return list


print(prime_factors(int(input('Enter number: '))))
