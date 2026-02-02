import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False]*N

def backtrack():
    if len(path) == M:
        sys.stdout.write(" ".join(map(str, path))+ "\n")
        return
    for i in range(N):
        if not visited[i]:
            path.append(nums[i])
            visited[i] = True

            backtrack()

            path.pop()
            visited[i] = False

path = []
backtrack()