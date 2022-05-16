# Как сделать проще - не знаю...
all_sum = 0


def nightmareterrible_sum(ntargs):
    # return(sum(ntargs))
    global all_sum
    s = sum(ntargs)
    print(f"промежуточная: {s}")
    all_sum += s
    print(f"итоговая: {all_sum}")


n = input("вводите числа через пробел. Для завершения ввода введите stop : ").split()
while True:
    lst = []
    for x in n:
        if str(x).isnumeric():
            lst.append(int(x))
        elif str(x).lower() == "stop":
            nightmareterrible_sum(lst)
            exit(0)
            break
    nightmareterrible_sum(lst)
    n = input().split()
