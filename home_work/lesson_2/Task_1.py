# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

def sum_of_digits(number):
    number = float(number) * 10 ** len(number)
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return int(sum)

num = input('Enter a number: ')
sum = sum_of_digits(num)

print(f"{num} -> {sum}")

