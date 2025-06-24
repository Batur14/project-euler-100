def palindrom(n):
    m=int(len(str(n)))
    b=0
    for a in range(int(m/2)):
        b=0
        if str(n)[0] == str(n)[5]:
            b+=1
        if str(n)[1] == str(n)[4]:
            b += 1
        if str(n)[2] == str(n)[3]:
            b += 1
        if b == 3:
            print(n)

for i in range(334,1000,1):
    for j in range(334,1000,1):
        x = i * j
        palindrom(x)