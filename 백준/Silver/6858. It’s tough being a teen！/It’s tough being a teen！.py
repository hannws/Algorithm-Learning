import sys
from collections import deque
input = sys.stdin.readline

todo = {1:[4, 7], 2:[1], 3:[4, 5], 4:[], 5:[], 6:[], 7:[]}
indegree = {1:1, 2:0, 3:0, 4:2, 5:1, 6:0, 7:1}

for _ in range(5):
    x = int(input())
    y = int(input())
    if x==0 and y ==0:
        break
    todo[x].append(y)
    indegree[y] += 1

dq = deque()

for i in range(1, 8):
    if indegree[i] ==0:
        dq.append(i)

result = []

while dq:
    dq = deque(sorted(dq))
    cur = dq.popleft()
    result.append(cur)

    for nxt in todo[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] ==0:
            dq.append(nxt)

if len(result) ==7:
    print(*result)
else:
    print("Cannot complete these tasks. Going to bed.")