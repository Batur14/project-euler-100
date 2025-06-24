def birinci(n):
    top = 0
    if n < 10:
        for i in str(n):
            if i == "1":
                top+=3
            elif i == "2":
                top+=3
            elif i == "3":
                top+=5
            elif i == "4":
                top+=4
            elif i == "5":
                top+=4
            elif i == "6":
                top+=3
            elif i == "7":
                top+=5
            elif i == "8":
                top+=5
            elif i == "9":
                top+=4
            return top

def gerikalan(n):
    top = 0
    b = 0
    if 10 <= n and n < 20:
        str(n)
        if n == "10":
            top+= 3
        elif n == "11":
            top+=6
        elif n == "12":
            top+=6
        elif n == "13":
            top+=8
        elif n == "14":
            top+=8
        elif n == "15":
            top+=7
        elif n == "16":
            top+=7
        elif n == "17":
            top+=9
        elif n == "18":
            top+=8
        elif n == "19":
            top+=8
        return top
    int(n)

    if 20 <= n and n <100:
        while not n % 10 ==0:
            n-=1
            b+=1
        if n == "10":
            top += 3
        elif n == "20":
            top += 6
        elif n == "30":
            top += 6
        elif n == "40":
            top += 5
        elif n == "50":
            top += 5
        elif n == "60":
            top += 5
        elif n == "70":
            top += 7
        elif n == "80":
            top += 6
        elif n == "90":
            top += 6
        a = top + birinci(b)
        return a
def ucuncu(n):
    top=0
    c=0
    b=0
    if 100 <= n < 1000:

        while  n % 100 == 0:
            if n < 100:
                break
            n-=100
            c+=1
        if c == 1:
            top+=7
        elif c == 2:
            top += 7 + 3
        elif c == 3:
            top += 7 + 5
        elif c == 4:
            top+=7+4
        elif c == 5:
            top+=7+4
        elif c == 6:
            top+=7+3
        elif c == 7:
            top+=7+5
        elif c == 8:
            top+=7+5
        elif c == 9:
            top+=7+4
        if n < 10:
            a = birinci(n)
        else:
            a=gerikalan((n))
        if a == None:
            a = 0
        d= a + top
        return d
a = 100
b= 10
x = 36
while a < 1000:
    x+=ucuncu(a)
    a+=1
while b < 100:
    x+=gerikalan(b)
    b+=1
print(x)