import sys
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    d = y - x

    n = int(math.sqrt(d))

    # 이동횟수에 따른 거리의 증가는 제곱과 관련 있다.
    # 2n-1 -> n*n , 2n -> n*(n+1), 2n+1 -> (n+1)*(n+1)
    # 주어진 거리가 어떤 n*n <= dis <= (n+1)*(n+1) 에 포함되는지 판단 필요

    if d == n * n:
        print(2 * n - 1)
    elif d <= n * (n + 1):
        print(2 * n)
    else:
        print(2 * n + 1)