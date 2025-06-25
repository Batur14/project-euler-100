import math
def prime(s):
    if s < 2:
        return False
    a = int(math.sqrt(s)) + 1
    for i in range(2,a):
        if s % i == 0:
            return False
    return True
def rotations(a):
    s= str(a)
    return[int(s[i:] + s[:i]) for i in range(len(s))]
def all(s):
    for i in rotations(s):
        if not prime(i):
            return False
    return True
x = 2
d = 0
for i in range(2,1000000):
    if all(i):
        d+=1
print(d)
