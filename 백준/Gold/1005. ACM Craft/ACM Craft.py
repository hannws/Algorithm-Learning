import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    N, K = map(int, input().split())
    buildtime = list(map(int, input().split()))
    beforebuilding = [[] for _ in range(N)]
    afterbuilding = [[] for _ in range(N)]
    memo = [0]*N

    dp = [0]*N
    for _ in range(K):
        x, y = map(int, input().split())
        beforebuilding[y-1].append(x-1)
        afterbuilding[x-1].append(y-1)
        memo[y-1] += 1
    
    goal = int(input()) - 1

    dq = deque()
    for i in range(N):
        if memo[i]==0:
            dq.append(i)

    while dq:
        curr = dq.pop()
        dp[curr] = max([dp[i] for i in beforebuilding[curr]], default=0) + buildtime[curr]

        for i in afterbuilding[curr]:
            memo[i] -= 1
            if memo[i] == 0:
                dq.append(i)
    print(dp[goal])