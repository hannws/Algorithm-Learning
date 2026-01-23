import sys
input = sys.stdin.readline

T = int(input())
dp = {1:1, 2:2, 3:4}
graph = [1,2,3]

def f(n):
    if dp.get(n, 0):
        return dp[n]

    total = 0
    for i in graph:
        total += f(n-i)
    
    dp[n] = total
    return total


for _ in range(T):
    n = int(input())
    print(f(n))