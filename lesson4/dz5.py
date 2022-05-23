from functools import reduce


def mul(a, b):
    return a * b


# В условии задачи было сказано использовать генератор, но не понятно, надо было использовать его или comprehention
# Я использовал comprehention
print(reduce(mul, [x for x in range(100, 1000 + 1) if x % 2 == 0]))