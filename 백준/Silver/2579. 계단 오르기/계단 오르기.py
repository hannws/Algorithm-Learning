import sys
input = sys.stdin.readline

N = int(input())
score = [0] + [int(input()) for _ in range(N)]
dp = [[0,0] for _ in range(N+1)]

if N >= 1:
    dp[1][0] = score[1]

if N >= 2:
    dp[2][0] = score[2]
    dp[2][1] = score[2] + score[1]

for i in range(3, N+1):
    dp[i][0] = max(dp[i-2][1],dp[i-2][0]) + score[i]
    dp[i][1] = dp[i-1][0] + score[i]

print(max(dp[N][0], dp[N][1]))