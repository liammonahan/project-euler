

sums = set()
abundant = []
for a in range(1, 28124):
    divs = sum([i for i in range(1, int(a // 2) + 1) if a % i == 0])
    if divs > a:
        abundant.append(a)

for i in abundant:
    for j in abundant:
        s = i + j
        if s <= 28124:
            sums.add(s)

total = 0
for i in range(1, 28124):
    if i not in sums:
        total += i
print(total)
