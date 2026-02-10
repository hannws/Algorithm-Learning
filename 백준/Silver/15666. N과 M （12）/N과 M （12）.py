import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(set(list(map(int, input().split()))))
nums.sort()
length = len(nums)

def backtrack(start):
    if len(path) == M:
        print(*path)
        return

    for i in range(start, length):
        path.append(nums[i])
        backtrack(i)
        path.pop()

path = []
backtrack(0)