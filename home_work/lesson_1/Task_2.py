# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not x and not y and not z):
                print(x, y, z)