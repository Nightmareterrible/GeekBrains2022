# В этой работе я хотел поизвращаяться и посмотреть, что я вынес из вебинара.
# (1) распаковка словаря в аргументы функции
# (2) создание целочисленного нового списка при помощи генератора
# (3) использование функций sum и min
# И конечно же нет ошибок по PEP 8
def my_func(a: int, b: int, c: int):
    """Находит сумму 2-х наибольших элементов из 3-х переданных"""
    return sum([a, b, c]) - min([a, b, c])  # (3)
    pass


numbers = input("Введите 3 числа, разделённые пробелом : ").split()
if len(numbers) != 3:
    print(f"Необходимо ввести 3 числа. Вы ввели {len(numbers)}")
    exit(3)
numbers = [int(x) for x in numbers]  # {2}
print(my_func(*numbers))  # (1)
