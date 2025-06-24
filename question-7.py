import math
x = 2
y = 1
while y <= 10001:
    for i in range(2,x+1):
        if math.sqrt(x) % i == 0:
            break
    y+=1
    elif math.sqrt(x) % i == 0:
        x+=1

print(x)