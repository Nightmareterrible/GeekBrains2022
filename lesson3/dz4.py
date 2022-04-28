def my_func(x, y):
    # Раскомментировав строку ниже, вы получите проверку правильности вычисления
    # return x**y
    res = 1
    for i in range(y, 0):
        res *= 1 / x
    return res


try:
    a, b = map(float, input("Введите 2 числа через пробел : ").split())
    if a < 0:
        raise Exception('Первое число не может быть отрицательным')
        # далее действие программы прервётся, 2-й IF недосягаем
    if b >= 0 or int(b) - b != 0:
        raise Exception('Второе число должно быть отрицательным и целым')
    b = int(b)
    print(my_func(a, b))
except ValueError as err:
    print(f"Необходимо ввести целое число, {str(err).split(':')[1]} - не число")
