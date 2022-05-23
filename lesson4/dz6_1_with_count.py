from itertools import count
from sys import argv
for el in count(int(argv[1])):
    if el > 15:
        break
    print(el)
