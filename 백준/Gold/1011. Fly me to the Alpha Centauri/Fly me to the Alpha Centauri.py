import sys
input = sys.stdin.readline

def maxmove(N):
    if dp.get(N, 0):
        return dp[N]
    incr = 0
    if N%2 == 0:
        incr = N//2
    else:
        incr = N//2 + 1
    dp[N] = dp[N-1] + incr
    return dp[N]


t = int(input())

dp = {1:1, 2:2}

for _ in range(t):
    start, end = map(int, input().split())
    dis = end - start
    
    success = False

    if dis == 1:
        success = True
        print(1)
    elif dis == 2:
        success = True
        print(2)

    move = 3
    while not success:
        if move <= dis <= maxmove(move):
            print(move)
            success = True
        move += 1