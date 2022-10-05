def my_func(string_val):
    for index in string_val:
        if not index.replace("-", "").isdigit():
            return []
    return string_val


def min_sum(val):
    art = my_func(val)
    if art:
        return min(art, key=int), max(art, key=int)
    else:
        return []

print(min_sum(input().split()))