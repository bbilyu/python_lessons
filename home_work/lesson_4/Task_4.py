# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
#
# in
# 0
# -1
# 4
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

import random


def polynomial_equations(file_name: str):
    print(f"Filling file {file_name}")
    with open(file_name, "w", encoding="utf-8") as output:
        for k in [int(input(f' Enter number №{n + 1} : ')) for n in range(random.randint(3, 5))]:
            if k > 0:
                list_tmp = []
                for j in reversed(range(k + 1)):
                    i = random.randint(0, 10)
                    if i > 0 and j > 0:
                        list_tmp.append(f"{i}*x^{j}")
                    elif i > 0:
                        list_tmp.append(f"{i}")
                    else:
                        pass
                for element in list_tmp:
                    if element != list_tmp[-1]:
                        output.write(f"{element} {random.choice(['-', '+'])} ")
                    else:
                        output.write(f"{element} ")
                output.write("= 0\n")
    print()


if __name__ == '__main__':
    polynomial_equations("poly_1.txt")
