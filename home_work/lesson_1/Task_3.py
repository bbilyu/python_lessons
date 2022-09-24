# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Enter the x value: '))
y = int(input('Enter the y value: '))

if x != 0 and y != 0:
    if x > 0 and y > 0:
        print("First quarter")
    elif x < 0 and y > 0:
        print("Second quarter")
    elif x < 0 and y < 0:
        print("Third quarter")
    elif x > 0 and y < 0:
        print("Fourth quarter")
elif  x != 0 and y == 0:
    print("The point is on the x axis")
elif  x == 0 and y != 0:
    print("The point is on the y axis")
else:
    print("Error, 0 entered!")
