from itertools import permutations

perm = permutations([0,1,2,3,4,5,6,7,8,9])
x = 0
for i in perm:
    x+=1
    if x == 1000000:
        print(i)
        break