def nightmareterrible_func(x: int, y: int) -> str:
    """Выполняет арифметическое деление A/B"""
    try:
        return str(x / y)
    except ZeroDivisionError as err:
        return str(err) + " (Деление на 0 невозможно)"


a = int(input("Введите первое число :"))
b = int(input("Введите второе число :"))
print("результат выполнения деления A/B : ", nightmareterrible_func(a, b))
