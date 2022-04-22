all_time = int(input("white time in seconds : "))
sec = all_time % 60
all_time //= 60
minutes = all_time % 60
all_time //= 60
hours = all_time % 24
all_time //= 60
days = all_time // 60 % 365
print("{:02}:{:02}:{:02}".format(hours, minutes, sec))  # PEP 8: E231 missing whitespace after ',' - needs space bar
print(f"{days:02} days {hours:02} hours {minutes:02} min {sec:02} sec")
