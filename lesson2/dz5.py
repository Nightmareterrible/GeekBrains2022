rating = [7, 5, 3, 3, 2]
tmp_list = []

while True:
    r = input("write new rating number or Enter for exit :")
    if len(r) == 0:
        break
    r = int(r)
    while len(rating) > 0:
        elem = rating[-1]
        if elem < r:
            tmp_list.append(elem)
            rating.pop()
        else:
            break
    tmp_list.append(r)
    tmp_list.extend(list(reversed(rating)))
    rating = list(reversed(tmp_list))
    tmp_list.clear()
    print(rating)
