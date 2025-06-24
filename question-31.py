say = 0
for i in range(0, 3):
    for j in range(0, 5):
        for k in range(0, 11):
            for a in range(0, 21):
                for b in range(0, 41):
                    for c in range(0, 101):
                        kal = i*100 + j*50 + k*20 + a*10 + b*5 + c*2
                        d = 200 - kal
                        if d >= 0:
                            say += 1
print(say)
