# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

number = int(input('Enter a number: '))
list = [round((1 + 1 / (n + 1)) ** (n + 1)) for n in range(number)]

print(f"{list} -> {sum(list)}")
