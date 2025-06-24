import math

def is_prime(s):
    if s < 2:
        return False
    if s == 2:
        return True
    if s % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(s)) + 1, 2):
        if s % i == 0:
            return False
    return True

max_len = 0
best_a = 0
best_b = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while True:
            val = n*n + a*n + b
            if is_prime(val):
                n += 1
            else:
                break
        if n > max_len:
            max_len = n
            best_a = a
            best_b = b

print(f"En uzun asal zinciri: {max_len} (a={best_a}, b={best_b})") 