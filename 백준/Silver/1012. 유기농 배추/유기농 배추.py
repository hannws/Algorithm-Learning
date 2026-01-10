import sys
sys.setrecursionlimit(10**6)
test_case = int(sys.stdin.readline())

def dfs(y, x):
    field[y][x] = 0
    for i, j in (1,0), (0,1), (-1,0), (0,-1):
        if 0 <= y+j < n and 0<= x+i < m and field[y+j][x+i]:
            dfs(y+j, x+i)

for _ in range(test_case):
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[0]*m for _ in range(n)]

    for _ in range(k):
        x,y = map(int, sys.stdin.readline().split())
        field[y][x] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if field[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)