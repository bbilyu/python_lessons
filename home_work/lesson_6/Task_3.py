# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
#
# out
#
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}



def check_names():
    while(True):
        tmp = 0
        names_tmp = sorted(input("Enter names: ").split())
        for name in names_tmp:
            if name.isdigit():
                tmp = 1
        if tmp == 1:
            print("Wrong!")
            continue
        else:
            break
    return names_tmp


def sorted_names(names: list):
    print({letter[:1].upper():sorted([name for name in names if letter[:1].upper() == name[:1].upper()]) for letter in names})


# _______________________________________________
# sorted_names(check_names())
#
#
# from itertools import groupby
#
#
# def thesaurus(*args):
#     if "" not in args:
#         return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
#     return "Error"


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))
