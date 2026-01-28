import sys
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(row)]
dis = [[-1]*col for _ in range(row)]

dq = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(row):
    for j in range(col):
        if grid[i][j] == 0:
            dis[i][j] = 0
        elif grid[i][j] == 2:
            dis[i][j] = 0
            dq.append((i, j))

while dq:
    x, y = dq.popleft()

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < row and 0 <= ny < col:
            if dis[nx][ny] == -1:
                dis[nx][ny] = dis[x][y] + 1
                dq.append((nx, ny))

for r in dis:
    print(*r)