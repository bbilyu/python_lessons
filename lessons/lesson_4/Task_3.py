from math import gcd

print("Введите два числа: ")
a = int(input("a = "))
b = int(input("b = "))


def nok(first, second):
    return (first * second) // gcd(first, second)


print(nok(a, b))
