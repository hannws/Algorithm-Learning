import sys
input = sys.stdin.readline

MOD = 1_000_000

def fib(n):
    # (F(n), F(n+1)) 반환
    if n == 0:
        return (0, 1)

    a, b = fib(n // 2)

    c = (a * ((2 * b - a) % MOD)) % MOD
    d = (a * a + b * b) % MOD

    if n % 2 == 0:
        return (c, d)
    else:
        return (d, (c + d) % MOD)

n = int(input())
print(fib(n)[0])