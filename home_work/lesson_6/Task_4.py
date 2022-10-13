# 4. * Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь, ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"
#
# out
#
# {'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']}, 'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']}, 'И': {'И': ['Илья Иванов']}, 'В': {'Ю': ['Юнона Ветрякова']}}


def check_input():
    while(True):
        tmp = 0
        names_surnames_tmp = sorted(input("Enter the names in two spaces 'Анна Савельева  Антон Серов': ").split("  "))
        for name in names_surnames_tmp:
            if name.isdigit():
                tmp = 1
        if tmp == 1:
            print("Wrong!")
            continue
        else:
            break
    return names_surnames_tmp


def name_surname_sorted(name_surname: list):
    print({letter_S.split()[1][:1].upper() : {letter_N.split()[0][:1].upper():sorted([name for name in name_surname if letter_N.split()[0][:1].upper() == name.split()[0][:1].upper() and letter_S.split()[1][:1].upper() == name.split()[1][:1].upper()]) for letter_N in name_surname if letter_N.split()[1][:1].upper() == letter_S.split()[1][:1].upper()} for letter_S in name_surname})


name_surname_sorted(check_input())
