n = input()
print(F"A sum for {n} + {n+n} + {n+n+n} is ", end="")
print(int(n) + int(n+n) + int(n+n+n))
count = len(n)
k = pow(10, count)
n1 = int(n)
n2 = n1 * k + n1
n3 = n2 * k + n1
print("another variant :", (n1 + n2 + n3))

n1 + n1 + n1 + n1*k + (n1*k + n1)*k
n1*3 + n1*k + n1*k*k + n1*k
n1*(k*2 + 3) + n1*k*k
n1*(k*2 + 3 + k*k)
p = n1*(k*(2 + k) + 3)
print("last variant :", p)
