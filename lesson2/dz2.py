# first_list = [1,2,3,False,[5,6],"7",'8',9.10]
first_list = []
while True:
    elem = input("add new element in list, or type Enter for complete list:")
    if len(elem) == 0:
        break
    first_list.append(elem)
print(f"source list : {first_list}")
for i in range(0, len(first_list), 2):
    first_list[i], first_list[i+1] = first_list[i+1], first_list[i]
print(f"changed list : {first_list}")
