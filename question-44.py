import math
def P(n):
    return int(n*(3*n-1)/2)
def check(n):
    a = 1 + 24*n
    b = math.isqrt(a)
    if b*b != a:
        return False
    return (1 + b) % 6 == 0
a = 2
condition = True
while condition:
    for i in range(1,a):
        n1 = P(a) + P(i)
        n2 = P(a) - P(i)
        if check(n1) and check(n2):
            print(n2)
            condition = False
            break
    a +=1

print(P(3))
print(check(P(6)))