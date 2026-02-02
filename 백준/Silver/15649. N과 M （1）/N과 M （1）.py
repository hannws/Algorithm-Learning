import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False]*(N+1)

def backtrack():
    if len(path) == M:
        print(*path)
    for i in range(1, N+1):
        if not visited[i]:
            path.append(i)
            visited[i] = True

            backtrack()

            path.pop()
            visited[i] = False

path = []
backtrack()