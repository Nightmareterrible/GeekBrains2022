f = open("dz1.txt", "w+", encoding="utf-8")

print("Начинаем запись в файл. Вводите строки. Для завершения введите пустую строку")
while 1 == 1:
    data = input()
    if data == "":
        break
    f.write(data + "\n")
answer = input("Ввод данных завершён. Вывести получившийся файл? Y/N ").upper()
if answer == "Y":
    f.seek(0)
    print(f.read())
f.close()
