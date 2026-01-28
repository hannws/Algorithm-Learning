import sys
from collections import deque
input = sys.stdin.readline

col, row = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(row)]
visited = [[False]*col for _ in range(row)]
dq = deque()
cnt = -1

for i in range(row):
    for j in range(col):
        if tomato[i][j] == 1:
            visited[i][j] = True
            dq.append((i,j))
        elif tomato[i][j] == -1:
            visited[i][j] = True

def onedaylater(dq):
    result = deque()
    while dq:
        r, c = dq.popleft()
        for ir, ic in ((1,0), (0,1), (-1,0), (0,-1)):
            nr = r+ir
            nc = c+ic
            if 0 <= nr < row and 0 <= nc < col:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    result.append((nr, nc))
    return result

while dq:
    dq = onedaylater(dq)
    cnt += 1

success = True
for i in visited:
    if 0 in i:
        success = False
        break

if success:
    print(cnt)
else:
    print(-1)