import sys
from heapq import heappop, heappush
input = sys.stdin.readline
MAX = float('inf')

node = int(input())
m = int(input())
edge = [tuple(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())

graph = [[] for _ in range(node+1)]
dis = [MAX]*(node+1)

for i, j, k in edge:
    graph[i].append((k, j))

hq = []
heappush(hq, (0,start))
dis[start] = 0

prev = [-1]*(node+1)

while hq:
    curr, idx = heappop(hq)

    if curr > dis[idx]:
        continue
    
    for cost, nxt in graph[idx]:
        total = curr + cost
        if dis[nxt] > total:
            prev[nxt] = idx
            dis[nxt] = total
            heappush(hq, (total, nxt))

path = []
cur = end
while cur != -1:
    path.append(cur)
    cur = prev[cur]
path.reverse()

print(dis[end])
print(len(path))
print(*path)