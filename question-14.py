def lon(n):
    b = 1
    while not n == 1:
        if n % 2 == 0:
            n = n/2
            b+=1
        elif n % 2 == 1:
            n = 3*n + 1
            b+=1
    return b
def lon1(n):
    b = 1
    x = n
    while not n == 1:

        if n % 2 == 0:
            n = n/2
            b+=1
        elif n % 2 == 1:
            n = 3*n + 1
            b+=1
    return x
a = 1
value = 0
higvalue = 0
c = 0
z=0
while a < 1000000:
    x = lon(a)
    y = lon(a+1)
    if x > y:
        value = x
    else:
        value = y

    if value > z:
        c = a
        z = lon(c)
        higvalue = lon1(c)
    a+=1
print(higvalue)