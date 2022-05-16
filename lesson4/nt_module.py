from random import randint


def get_random_list():
    return [randint(0, 200) for _ in range(randint(10, 20))]  # было i, но выдавало ошибку PEP-8
