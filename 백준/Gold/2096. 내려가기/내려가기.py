import sys
input = sys.stdin.readline

N = int(input())

max_dp = [0, 0, 0]
min_dp = [0,0,0]

for i in range(N):
    a, b, c = map(int, input().split())

    if i == 0:
        max_dp = [a, b, c]
        min_dp = [a, b, c]
    else:
        prev_max = max_dp[:]
        prev_min = min_dp[:]

        max_dp[0] = a+max(prev_max[0], prev_max[1])
        max_dp[1] = b+ max(prev_max)
        max_dp[2] = c + max(prev_max[1], prev_max[2])

        min_dp[0] = a + min(prev_min[0], prev_min[1])
        min_dp[1] = b + min(prev_min)
        min_dp[2] = c + min(prev_min[1], prev_min[2])

print(max(max_dp), min(min_dp))