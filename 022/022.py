names = []
with open('names.txt', 'r') as f:
    for line in f:
        line = line.strip().split(',')
        _n = [name.strip('"') for name in line]
        names.extend(_n)

total = 0
for i, name in enumerate(sorted(names), start=1):
    total += sum([ord(c) - 64 for c in name]) * i
print(total)
