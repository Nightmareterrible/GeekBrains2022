import itertools
from sys import argv
from nt_module import get_random_list

error_msg = "Ошибка ввода данных. Необходимо ввести 1 целое число (количество элементов). Введено чисел : " \
            + str(len(argv)-1)
error_msg_value = "Ошибка ввода данных. Ожидались целое число"


def get_elems():
    return itertools.cycle(get_random_list()) if len(argv) > 1 else itertools.cycle([error_msg])


count = 0
try:
    for i in get_elems():
        print(i)
        if type(i) != int or count > int(argv[1]):
            break
        count += 1
except ValueError:
    print(error_msg_value)
