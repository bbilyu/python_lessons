from secrets import choice


def fill_list(num):
    array = [i for i in range(num + 1)]
    array.remove(choice(array))
    return array


# print(fill_list(int(input("Enter the positive number"))))


def check_number(array):
    for i in range(1, len(array)):
        if array[i] - 1 != array[i - 1]:
            return array[i] - 1
    return -1


array = fill_list(int(input("Enter the positive number")))
print(array)

print(check_number(array))
