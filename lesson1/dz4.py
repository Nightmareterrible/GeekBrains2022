n = int(input("please write a number with a lot digits : "))
max_digit = 0
while n > 0:
    if n % 10 > max_digit:
        max_digit = n % 10
    n //= 10
print(f" the biggest digit is {max_digit}")
