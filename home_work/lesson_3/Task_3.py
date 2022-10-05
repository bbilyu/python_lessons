# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
#
# in
# 11
# out
# 1011

def decimal_to_binary(number: int):
    binary_number = []
    while number > 0:
        binary_number.insert(0,number % 2)
        number //= 2
    return binary_number


print(*decimal_to_binary(int(input('Enter an integer: '))),sep="")
