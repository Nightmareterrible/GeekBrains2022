from nt_module import *
lst = get_random_list()
print(f"Исходный список : {lst}")
# Создаём zip-ом список кортежей, каждый из которых состоит из обычного и "сдвинутого" списка (i, i+1), (i+1, i+2) и т.д
lst2 = [nxt for prev, nxt in zip(lst, lst[1:]) if nxt > prev]
print(f"Новый список    : {lst2}")
exit(0)

# старое решение при помощи цикла
lst2 = []
prev = lst[0]
for i in lst[1:]:
    if i > prev:
        lst2.append(i)
    prev = i
print(f"Новый список    : {lst2}")
