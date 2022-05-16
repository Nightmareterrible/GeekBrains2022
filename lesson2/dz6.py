tovars = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]
while True:
    name = input("Управление товарами магазина. Для начала добавления товара введите его имя \n" +
                 "Для заверешения ввода и просмотра результатов нажмите Enter :")
    if name == "":
        break
    cost = int(input("введите цену : "))
    count = int(input("введите количество : "))
    unit = input("введите единицу измерения : ")
    tovars.append((len(tovars)+1, {"название": name, "цена": cost, "количество": count, "eд": unit}))


my_dict = dict.fromkeys(tovars[0][1].keys())

print(my_dict)
for i in tovars:
    dict1 = i[1]
    for key, v in dict1.items():
        if my_dict[key] is None:
            my_dict[key] = list([v])
        else:
            my_dict[key].append(v)
print(my_dict)
exit(0)

# Код ниже- не рабочий. Оказывается у списсков значениях dict одинаковый адрес в памяти. И у всех ключей один value
my_dict = dict.fromkeys(tovars[0][1].keys(), list([]).copy())
# Если написать просто  ..., []  , то будет ошибка в v.append(1)
for elem in tovars:
    dict2 = elem[1]
    print(dict2)
    for key in dict2:
        # v = list(my_dict[key])
        # v.append(1)
        print(dict2[key])
        print("my_dict[key] : ", my_dict[key])
        my_dict[key].append(dict2[key])
        print("dict : ", my_dict)
        # v.extend(1)
        # my_dict[key].extend(dict2[key])
print(my_dict)
