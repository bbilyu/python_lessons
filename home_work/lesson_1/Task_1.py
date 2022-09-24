# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

number = int(input('Enter a number: '))

week_day = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

if number in range(1,6):
    print(f"{week_day[number-1]} -> Workday")
elif number in range(6,8):
    print(f"{week_day[number-1]} -> Weekend")
else:
    print("It's not a day of the week!")
