import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, k = map(int, input().split())
visited = [[True]*m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    visited[r-1][c-1] = False

def dfs(i, j):
    ret = 1
    visited[i][j] = True

    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for di, dj in move:
        ni = i + di
        nj = j + dj
        if 0<=ni<n and 0<=nj<m:
            if visited[ni][nj] == False:
                ret += dfs(ni, nj)

    return ret

waste = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            waste = max(waste, dfs(i, j))

print(waste)