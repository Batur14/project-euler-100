import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
a = 9
b = True

while b:
    if not prime(a):
        durum=False
        for i in range(3,a,2):
            if prime(i):
                j = 1
                while j*j*2 < a:
                    if i + j*j*2 == a:
                        durum= True
                        break
                    j+=1
                if durum:
                    break
        if not durum:
            print(a)
            break
    a+=2

