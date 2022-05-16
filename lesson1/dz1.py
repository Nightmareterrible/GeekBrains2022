a = 8
b = "5"
# print(a-b) # TypeError: unsupported operand type(s) for -: 'int' and 'str'
# inline comment should start with #_ (# and space symbol)
a += 1  # python does not support ++, sob sob
print(a)
# b += 1  #TypeError: can only concatenate str (not "int") to str
print(b)
a -= 1
print(a)
# b -= 1  #TypeError: unsupported operand type(s) for -=: 'str' and 'int'
print(b)
b += b
print(b)

name = input("say your name :")
print(f"hello, {name}, ", end="")  # end=None does not works
rate = int(input("rate this program by mark between 0 and 10 :"))
if rate in range(10):
    print("thank a lot !")
else:
    print("number is not supported")
