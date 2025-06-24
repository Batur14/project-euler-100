def square(n):
    x=0
    for i in str(n):
        x+= int(i)**2
    return x
def a(n):

    while not n == 89 or 1:
        n = square(n)
        if n == 1:
            return 1
        elif n == 89:
            return 89
b=1
c=0
while b < 10000000:
    if a(b) ==89:
        c+=1
    b+=1
print(c)