from sys import argv
error_msg = "Ошибка ввода данных. Необходимо ввести 3 целых числа. Введено чисел : " + str(len(argv)-1)
error_msg_value = "Ошибка ввода данных. Ожидались 3 целых числа"


def zp():
    try:
        return int(argv[1]) * int(argv[2]) + int(argv[3]) if len(argv) > 3 else error_msg
    except ValueError:
        return error_msg_value


print(zp())
