import math

a = int(input("Введите результат 1-го дня (км): "))
b = int(input("Введите требуемый результат (км): "))
result = math.ceil(math.log(b/a, 1.1) + 1)
print(result)

i = 1
# print(f"{i}-й день, {a} километров")
while a < b:
    a *=  1.1
    i += 1
    # print(f"{i}-й день, {a} километров")
# print(i)

