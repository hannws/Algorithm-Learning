import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def backtrack():
    if len(path) == M:
        sys.stdout.write(" ".join(map(str, path))+ "\n")
        return
    for i in range(1, N+1):
        path.append(i)
        backtrack()
        path.pop()

path = []
backtrack()