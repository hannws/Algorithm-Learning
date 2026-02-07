import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
dis = [-1]*100001
dq = deque()
dq.append(N)
dis[N] = 0

while dq:
    idx = dq.popleft()

    if idx == K:
        break

    for cost, nxt in ((1, idx+1), (1, idx-1), (0, idx*2)):
        total = dis[idx] + cost
        if 0<= nxt <= 100000 and (dis[nxt] == -1 or dis[nxt] > total):
            dis[nxt] = total
            if cost == 0:
                dq.appendleft(nxt)
            else:
                dq.append(nxt)

print(dis[K])