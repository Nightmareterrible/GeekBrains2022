# Я не могу понять - я выполнил 6-ю или 7-ю. Одинаковые условия, не могу понять чего от меня хотят )))
def int_func(*ntargs):
    lst = []
    for x in ntargs:
        lst.append(str(x).capitalize())
    return " ".join(lst)


# Строка print(*fruits) передаёт все элементы списка fruits в вызов print() как отдельные аргументы,
# поэтому нам даже не нужно знать, сколько элементов в списке.
# не нашёл этого в методичке, почитал здесь :
# https://tproger.ru/translations/asterisks-in-python-what-they-are-and-how-to-use-them/
print(int_func(*input("введите слова, разделённые пробелом : ").split()))
