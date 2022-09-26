# * 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

position_one = int(input('Position one: '))
position_two = int(input('Position two: '))
number_of_elements = int(input('Number of elements: '))
list = [n for n in range(-number_of_elements, number_of_elements + 1)]
product_of_list_items = list[position_one - 1] * list[position_two - 1]

print(f"{list} -> {product_of_list_items}")
