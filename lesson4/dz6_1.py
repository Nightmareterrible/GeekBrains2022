from sys import argv
error_msg = "Ошибка ввода данных. Необходимо ввести 1 целое число. Введено чисел : " + str(len(argv)-1)
error_msg_value = "Ошибка ввода данных. Ожидались целое число"


def get_elems():
    try:
        return iter(range(int(argv[1]), 15)) if len(argv) > 1 else iter([error_msg])
    except ValueError:
        return iter([error_msg_value])


for i in get_elems():
    print(i)
