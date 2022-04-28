seasons_list = ["winter", "spring", "summer", "autumn"]
seasons_dict = {0: "winter", 1: "spring", 2: "summer", 3: "autumn"}
month = int(input("write month number (1-12) :"))
print(f"it's {seasons_dict[month//3]}")
print(f"it's {seasons_list[month//3]}")
