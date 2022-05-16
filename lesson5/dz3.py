summ, count = 0, 0
with open('dz3.txt', 'r', encoding="utf-8") as f:
    for line in f.read().splitlines():
        if len(line.strip()) == 0:
            continue
        sotrud = line.split()
        if float(sotrud[1]) < 20000:
            print(f"{sotrud[0]}  имеет зп меньше 20 000")
        summ += float(sotrud[1])
        count += 1
print(f"Средняя зп равна : {summ/count}")
