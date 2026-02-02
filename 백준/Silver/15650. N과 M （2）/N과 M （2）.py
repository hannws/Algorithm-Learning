import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def backtrack(start):
    if len(path) == M:
        print(*path)
    for i in range(start, N+1):
        path.append(i)
        backtrack(i+1)
        path.pop()


path = []
backtrack(1)