def can(n):
    a=1
    b=0
    c=1
    d=0
    while a < n/2+1:
        if n % a == 0:
            b+=a
        a+=1
    while c < b/2+1:
        if b % c == 0:
            d+=c
        c+=1
    if not n==b:
        if n == d:
            print(n)
            return n
        else:
            return 0
    else:
        return 0
x = 0
top=0
while x < 10000:
    top+=can(x)
    x+=1
print(top)