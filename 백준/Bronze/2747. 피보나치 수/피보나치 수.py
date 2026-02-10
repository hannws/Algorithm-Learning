import sys
input = sys.stdin.readline

n = int(input())
dp = {0:0, 1:1}

for i in range(1, n):
    dp[i+1] = dp[i] + dp[i-1]

print(dp[n])