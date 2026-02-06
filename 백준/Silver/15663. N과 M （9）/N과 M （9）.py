import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False]*N

def backtrack():
    if len(path) == M:
        sys.stdout.write(" ".join(map(str, path))+'\n')
        return
    
    prev = None
    for i in range(N):
        if visited[i]:
            continue
        if prev == nums[i]:
            continue

        visited[i] = True
        path.append(nums[i])
        prev = nums[i]

        backtrack()

        visited[i] = False
        path.pop()



path = []
backtrack()