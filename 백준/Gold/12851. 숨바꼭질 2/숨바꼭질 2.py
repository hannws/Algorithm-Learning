import sys
from collections import deque
from math import inf
input = sys.stdin.readline

N, K = map(int, input().split())

def bfs(start, end):

    if start == end:
        return (0, 1)

    dis = [-1]*100001
    dis[start] = 0
    dq = deque()
    dq.append(start)
    stopsign = inf
    cnt = 0

    while dq:
        idx = dq.popleft()

        if dis[idx] > stopsign:
            continue
        elif dis[idx] == stopsign:
            if idx == end:
                cnt += 1
        else:
            for nxt in (idx+1, idx-1, idx*2):
                if 0<= nxt <= 100000:
                    if dis[nxt] == -1:
                        dis[nxt] = dis[idx] + 1
                        dq.append(nxt)
                        if nxt == end:
                            stopsign = dis[nxt]
                    elif dis[nxt] == dis[idx] + 1:
                        dq.append(nxt)
    return (stopsign, cnt)

t, path = bfs(N, K)
print(t)
print(path)