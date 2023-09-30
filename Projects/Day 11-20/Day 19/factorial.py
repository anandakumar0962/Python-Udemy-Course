n = int(input())
x = n
for i in range(1, n):
    x *= (n-i)
print(x)