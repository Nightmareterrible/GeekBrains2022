import requests as requests

# делать свой файл мне лень... А вот скачать книгу и посчитать в ней количество слов - это уже интересно
# меняйте число, чтобы получить другую книгу в формате txt
r = requests.post("https://tululu.org/txt.php?id=18919")
f = open("dz2.txt", "w+", encoding="utf-8")
f.write(r.text)
print("книга скачана")
f.seek(0)
words, lines = 0, 0
ignored = list('–,.?!')
ignored.append('')
while 1 == 1:
    line = f.readline()
    if not line:
        break
    lines += 1
    # words += len(line.split())  # этот метод не очень точный, т.к. в тексте могут быть пустые строки, дефисы и прочее
    lst = [ww for ww in line.split() if ww not in ignored]
    words += len(lst)
print(f"Количество строк : {lines}, количество слов : {words}")
f.close()
