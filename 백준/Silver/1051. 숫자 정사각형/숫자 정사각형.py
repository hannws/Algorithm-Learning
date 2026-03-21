import sys
input = sys.stdin.readline

n, m = map(int, input().split())

rec = [list(map(int, input().rstrip())) for _ in range(n)]
maxlen = 0

def calsq(i, j, x):
    if i + x >= n:
        return False
    
    curr = rec[i][j]
    return (curr == rec[i+x][j] and curr == rec[i+x][j+x])

for i in range(n):
    if (len(rec[i]) == len(set(rec[i]))):
        continue
    if (n-1-maxlen <= i):
        break

    for j in range(m-maxlen):
        prev = rec[i][j]
        for k in range(1, m-j):
            if k <= maxlen:
                continue
            if prev != rec[i][j+k]:
                continue
            if calsq(i, j, k):
                maxlen = k

print((maxlen+1)**2)