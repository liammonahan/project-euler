
def nxt(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n+1


def printseq(lst):
    lst = [str(i) for i in lst]
    print(' -> '.join(lst))


def calclen(i):
    n = i
    cnt = 1
    while n != 1:
        n = nxt(n)
        cnt += 1
    return cnt - 1


longest_start = 0
longest_len = 0
for i in range(1, 1000000):
    cnt = calclen(i)
    if cnt > longest_len:
        longest_len = cnt
        longest_start = i
print(f'{longest_start} is the longest sequence with a count of {longest_len}')
