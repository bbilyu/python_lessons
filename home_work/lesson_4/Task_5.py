# 5. ** Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
#
# in
# "poly.txt"
# "poly_2.txt"
#
# out
# The contents of the files do not match!

from Task_4 import polynomial_equations
import random


def merging_equations(first_file_name: str, second_file_name: str, output_file: str):
    if sum(1 for line in open(first_file_name)) == sum(1 for line in open(second_file_name)):
        with open(output_file, "w", encoding="utf-8") as output, \
                open(first_file_name, "r", encoding="utf-8") as my_f_1, \
                open(second_file_name, "r", encoding="utf-8") as my_f_2:
            list_tmp = []
            n = 0
            for i in my_f_2:
                list_tmp.append(i)
            for j in my_f_1:
                output.write(f"{j[:-4]}{random.choice(['-', '+'])} {list_tmp[n]}")
                n += 1
    else:
        print("The contents of the files do not match!")


polynomial_equations("poly_1.txt")
polynomial_equations("poly_2.txt")
merging_equations("poly_1.txt", "poly_2.txt", "poly_sum.txt")
