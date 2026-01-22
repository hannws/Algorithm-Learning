import sys
input = sys.stdin.readline

N = int(input())
score = [0] + [int(input()) for _ in range(N)]
dp = [[0,0] for _ in range(N+1)]
dp[N][1] = score[N]


def dfs(idx, cnt):

    if cnt==0:
        graph = [0]
    else:
        graph = [0, 1]

    for i in graph:
        nxt = idx-2+i
        nct = 1-i
        if nxt <= 0:
            continue
        
        current = dp[idx][cnt] + score[nxt]
        comp = dp[nxt][nct]

        if current > comp:
            dp[nxt][nct] = current
            dfs(nxt, nct)
            


dfs(N, 1)
print(max(map(max, dp)))