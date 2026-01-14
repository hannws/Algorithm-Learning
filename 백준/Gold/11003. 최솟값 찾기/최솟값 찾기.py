import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
A = list(map(int, input().split()))

dq = deque()
data = []

for i in range(len(A)):
    while dq and A[dq[-1]] >= A[i]:
        dq.pop()

    dq.append(i)

    if dq[0] <= i - l:
        dq.popleft()
    
    data.append(A[dq[0]])

print(*data)