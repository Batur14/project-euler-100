import math
def prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return 0
    return n
a = 2000000
top = 0
for i in range(2,a,1):
    top+=prime(i)
print(top)