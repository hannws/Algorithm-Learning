import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())
dq = deque()
dq.append((0, A))

while dq:
    cost, value = dq.popleft()
    
    for i in (value*10+1, value*2):
        if i < B:
            dq.append((cost+1, i))
        elif i==B:
            print(cost+2)
            sys.exit(0)
print(-1)