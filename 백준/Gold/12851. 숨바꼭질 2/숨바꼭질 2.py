import sys
from collections import deque
from math import inf
input = sys.stdin.readline

N, K = map(int, input().split())

def bfs(start, end):
    dis = [-1]*100001
    ways = [0]*100001

    dis[start] = 0
    ways[start] = 1
    dq = deque([start])

    while dq:
        x = dq.popleft()

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000:
                if dis[nx] == -1:
                    dis[nx] = dis[x] + 1
                    ways[nx] = ways[x]
                    dq.append(nx)
                elif dis[nx] == dis[x] + 1:
                    ways[nx] += ways[x]
    return dis[end], ways[end]

t, path = bfs(N, K)
print(t)
print(path)