a = 0
x=28433
y=""
list = []
while a < 7830457:
    x*=2
    y = ""
    if len(str(x)) > 10:
        for i in str(x):
            list.append(i)

            while list.count("0") + list.count("1") + list.count("2") +list.count("3") + list.count("4") + list.count("5") + list.count("6") + list.count("7") + list.count("8") + list.count("9") > 10:
                list.pop(0)
        for i in list:
            y.format(str)
            y+= i
        x = int(y)



    a+=1
print(x+1)