subjects = dict()
with open("dz6_in.txt", "r", encoding="utf-8") as f:
    for line in f.read().splitlines():
        subject = line.split(":")
        nums = map(int, [elem for elem in
                         [''.join([Z for Z in x if Z.isdigit()]) for x in subject[1].split()] if elem != ''
                         ])
        # print(list(nums))
        subjects[subject[0]] = sum(nums)
print(subjects)
