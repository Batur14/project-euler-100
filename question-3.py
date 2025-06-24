import math
x=600851475143
y=2

while y< math.sqrt(x):
    if x % y == 0:
        for i in range(2,y):
            if y%i==0:
                break
        else:
            print(y)
    y+=1