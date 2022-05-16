def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
        yield f


print(list(fact(5)))
for el in fact(5):
    print(el)
