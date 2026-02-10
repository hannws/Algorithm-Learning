import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(set(list(map(int, input().split()))))

def backtrack():
    if len(path) == M:
        print(*path)
        return

    for i in nums:
        path.append(i)
        backtrack()
        path.pop()

path = []
backtrack()