import math

for a in range(1,1000,1):
    for b in range(1,1000,1):
        for c in range(1,1000,1):
            if a+ b + c == 1000 and math.pow(a,2) + math.pow(b,2) == math.pow(c,2):
                print(a,b,c)