import sys
from collections import deque
input = sys.stdin.readline

start, end = map(int, input().split())

def bfs(start, end):
    dist = [-1]*100001
    dq = deque()

    dq.append(start)
    dist[start] = 0

    while dq:
        x = dq.popleft()

        if x == end:
            return dist[x]
        
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=100000 and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                dq.append(nx)
    return -1

print(bfs(start, end))