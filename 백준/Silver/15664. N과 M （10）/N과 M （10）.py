import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))

def backtrack(start):
    if len(path) == M:
        print(*path)
        return

    prev = -1
    for i in range(start, N):
        if nums[i] == prev:
            continue
        prev = nums[i]

        path.append(nums[i])
        backtrack(i+1)
        path.pop()

path = []
backtrack(0)