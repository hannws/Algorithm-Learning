import sys
input = sys.stdin.readline

size, t = map(int, input().split())
sumofnums = [[0]*(size+1) for _ in range(size+1)]

for i in range(1, size+1):
    row = list((map(int, input().split())))
    for j in range(1, size+1):
        sumofnums[i][j] = sumofnums[i-1][j] + sumofnums[i][j-1] - sumofnums[i-1][j-1] + row[j-1]


for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    result = sumofnums[x2][y2] - sumofnums[x1-1][y2] - sumofnums[x2][y1-1] + sumofnums[x1-1][y1-1]
    print(result)