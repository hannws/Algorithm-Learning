import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())
start = int(input())

distance = [float('INF')]*(N+1)
distance[start] = 0

graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j, k = map(int, input().split())
    graph[i].append((k, j))

hq = []
heappush(hq, (0, start))

while hq:
    current_cost, idx = heappop(hq)

    if current_cost > distance[idx]:
        continue

    for cost, nxt in graph[idx]:
        new_cost = current_cost + cost
        if new_cost < distance[nxt]:
            distance[nxt] = new_cost
            heappush(hq, (new_cost, nxt))

for i in range(1, N+1):
    print(distance[i] if distance[i] != float('inf') else "INF")