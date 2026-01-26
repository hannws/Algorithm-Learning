import sys
from collections import deque
input = sys.stdin.readline

size = int(input())
game = [list(map(int, input().split())) for _ in range(size)]
visited = [[False]*size for _ in range(size)]

dq = deque()
dq.append((0,0))
visited[0][0] = True
success = False

while dq:
    x, y = dq.popleft()
    move = game[y][x]

    for ix, iy in [(move, 0), (0, move)]:
        nx = x + ix
        ny = y + iy
        
        if nx == size-1 and ny == size -1:
            success = True
            break

        if 0<= nx < size and 0<=ny<size and not visited[ny][nx]:
            visited[ny][nx] = True
            dq.append((nx, ny))

if success:
    print("HaruHaru")
else:
    print("Hing")