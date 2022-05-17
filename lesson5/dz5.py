from random import randint

with open("dz5_out.txt", "w", encoding="utf-8") as w:
    for i in range(0, randint(0, 100)):
        w.write(str(randint(0, 100)) + " ")

with open("dz5_out.txt", "r", encoding="utf-8") as f:
    print(f"Исходный файл :{f.read()}")
    f.seek(0)
    print(f"Сумма чисел : {sum(map(int,f.read().split()))}")
