# я плохо знаю английский, поэтому на этот раз будет русский текст
выручка = int(input("введите выручку фирмы :"))
издержки = int(input("введите издержки фирмы :"))
разница = выручка - издержки
if разница > 0:
    print("Рады сообщить, что ваша фирма работает с прибылью")
elif разница < 0:
    print("Вынуждены сказать, что ваша фирма убыточна")
else:
    print("Доходы и расходы совпадают")