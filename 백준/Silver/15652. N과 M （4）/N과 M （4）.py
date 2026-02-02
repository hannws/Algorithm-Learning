import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def backtrack(start):
    if len(path) == M:
        sys.stdout.write(" ".join(map(str, path))+ "\n")
        return
    for i in range(start, N+1):
        path.append(i)
        backtrack(i)
        path.pop()

path = []
backtrack(1)