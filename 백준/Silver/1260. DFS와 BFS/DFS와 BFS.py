import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
graph = list(map(sorted, graph))
dfsvisited = [False]*(N+1)
bfsvisited = [False]*(N+1)

dfsresult= []
bfsresult = []
dq = deque()

def dfs(start):
    dfsvisited[start] = True
    dfsresult.append(start)

    for i in graph[start]:
        if dfsvisited[i] == False:
            dfs(i)

def bfs(start):
    dq.append(start)
    bfsvisited[start] = True
    while dq:
        curr = dq.popleft()
        bfsresult.append(curr)
        
        for i in graph[curr]:
            if not bfsvisited[i]:
                bfsvisited[i] = True
                dq.append(i)

dfs(V)
bfs(V)

print(*dfsresult)
print(*bfsresult)