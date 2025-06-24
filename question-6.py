import math

x=0
y=0
sum=0

for i in range(1,101):
    x= i**2
    sum-=x
    print(sum)
for n in range(1,101):
    y+= n
y**=2
sum+=y
print(sum)


