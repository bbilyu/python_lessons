# 1. Напишите программу, которая принимает на вход два числа
#    и проверяет, является ли одно число квадратом другого.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a == b * b or b == a * a:
    print("Является")
else:
    print("Не является")