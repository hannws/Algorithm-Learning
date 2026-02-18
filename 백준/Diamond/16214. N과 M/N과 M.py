import sys
import math
input = sys.stdin.readline

#오일러 피 함수
def phi(x):
    result = x
    p = 2
    
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            result -= result // p
        p += 1
    
    if x > 1:
        result -= result // x
    
    return result

def solve(n, m):
    if m == 1:
        return 0
    
    phim = phi(m)
    expo = solve(n, phim)

    if (math.gcd(n, m) == 1):
        return pow(n, expo, m)
    else:
        return pow(n, expo + phim, m)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))