# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N



number = int(input('Введите число: '))
print(*range(-number,number+1))