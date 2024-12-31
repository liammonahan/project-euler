
import collections


memo = collections.defaultdict(list)
amicable = set()

for a in range(1, 10000):
    da = sum([i for i in range(1, int(a // 2) + 1) if a % i == 0])
    if da != a:
        memo[da].append(a)

for a, vals in memo.items():
    for v in vals:
        if v in memo and a in memo[v]:
            amicable.add(a)
            amicable.add(v)

print(sum(amicable))
