# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

def factorial(number):
    factorial = 1
    while number != 1:
        factorial *= number
        number -= 1
    return factorial

num = int(input('Enter a number: '))
list = [factorial(i + 1) for i in range(num)]

print(f'{num} -> {list}')
