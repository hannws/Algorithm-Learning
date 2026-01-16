import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
topop = list(map(int, input().split()))

dq = deque(i+1 for i in range(N))
cnt = 0

for i in topop:
    location = dq.index(i)

    if location <= N//2:
        dq.rotate(-location)
        cnt += location
    else:
        dq.rotate(N-location)
        cnt += N-location
    
    dq.popleft()
    N -= 1
print(cnt)