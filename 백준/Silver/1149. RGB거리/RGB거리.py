import sys
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    curr = sorted([(value, idx) for idx, value in enumerate(dp[i-1])])
    for j in range(3):
        if j == curr[0][1]:
            dp[i][j] += curr[1][0]
            continue
        dp[i][j] += curr[0][0]

print(min(dp[N-1]))