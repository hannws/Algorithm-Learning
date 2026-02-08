import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
node = [-1]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dq = deque([1])
node[1] = 0

while dq:
    x = dq.popleft()

    for i in graph[x]:
        if node[i] == -1:
            node[i] = x
            dq.append(i)

for i in node[2:]:
    print(i)