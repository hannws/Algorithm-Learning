import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dq = deque()
dq.append((0,0,1))

while dq:
    x, y, cost = dq.popleft()
    if (x==n-1) and (y==m-1):
        print(cost)
        break

    cost += 1
    for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
        if 0<=nx<n and 0<=ny<m:
            if maze[nx][ny] and visited[nx][ny] == False:
                dq.append((nx, ny, cost))
                visited[nx][ny] = True