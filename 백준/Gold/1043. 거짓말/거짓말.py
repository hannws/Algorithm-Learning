import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
knowtruth = [False]*(N+1)
party = [1]*(M)
dq = deque()

p = list(map(int, input().split()))
if p[0] > 0:
    for i in p[1:]:
        knowtruth[i] = True
        dq.append(i)

member = []
for i in range(M):
    a = list(map(int, input().split()))
    member.append(a[1:])

while dq:
    idx = dq.popleft()

    for i in range(M):
        if party[i] and idx in member[i]:
            party[i] = 0
            for j in member[i]:
                if not knowtruth[j]:
                    knowtruth[j] = True
                    dq.append(j)

print(sum(party))