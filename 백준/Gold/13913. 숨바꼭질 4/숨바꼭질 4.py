import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

def bfs(start, end):
    dis = [-1]*100001
    prev = [-1]*100001

    dis[start] = 0
    dq = deque([start])
    
    while dq:
        x = dq.popleft()

        if x == end:
            break
        
        for nx in (x+1, x-1, x*2):
            if 0<= nx <= 100000 and dis[nx] == -1:
                dis[nx] = dis[x] + 1
                prev[nx] = x
                dq.append(nx)
    
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()

    return dis[end], path

t, p = bfs(N, K)
print(t)
print(*p)