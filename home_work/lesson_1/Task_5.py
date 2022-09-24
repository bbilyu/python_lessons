# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

x_A = int(input('Enter the x coordinate of point A: '))
y_A = int(input('Enter the y coordinate of point A: '))
x_B = int(input('Enter the x coordinate of point B: '))
y_B = int(input('Enter the y coordinate of point B: '))

distance = int(((x_B -x_A)**2 + (y_B-y_A)**2)**0.5*100)/100

print(f"A ({x_A},{y_A}); B ({x_B},{y_B}) -> {distance}")
