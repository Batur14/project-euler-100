def is_abundant(n):
    return sum(i for i in range(1, n // 2 + 1) if n % i == 0) > n

LIMIT = 28123

abundant_numbers = [i for i in range(1, LIMIT + 1) if is_abundant(i)]

abundant_sums = set()
for i in abundant_numbers:
    for j in abundant_numbers:
        if i + j <= LIMIT:
            abundant_sums.add(i + j)

all_numbers = set(range(1, LIMIT + 1))
non_abundant_sums = all_numbers - abundant_sums

print(sum(non_abundant_sums))