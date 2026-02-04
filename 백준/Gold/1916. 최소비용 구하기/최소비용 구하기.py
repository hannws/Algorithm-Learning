import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
M = int(input())
info = [tuple(map(int, input().split())) for _ in range(M)]
start, end = map(int, input().split())

MAX = float('inf')
distance = [MAX]*(N+1)
distance[start] = 0

graph = dict()
for i, j, k in info:
    graph.setdefault(i, []).append((j, k))

hq = []
heappush(hq,(0, start))

while hq:
    cost, now = heappop(hq)

    if cost > distance[now]:
        continue

    for nxt, w in graph.get(now, []):
        new_cost = cost + w
        if new_cost < distance[nxt]:
            distance[nxt] = new_cost
            heappush(hq, (new_cost, nxt))

print(distance[end])