import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

cards = [int(input()) for _ in range(n)]
result = []
path = []
visited = [False]*n


def backtrack():
    if len(path) == k:
        result.append("".join(map(str, path)))
        return
    
    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        path.append(cards[i])

        backtrack()

        path.pop()
        visited[i] = False


backtrack()

print(len(set(result)))