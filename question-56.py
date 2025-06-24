value =0
for a in range(1,100):
    for b in range(1,100):
        x = a**b
        top=0
        for i in str(x):
            top+=int(i)
        if top > value:
            value = top
print(value)