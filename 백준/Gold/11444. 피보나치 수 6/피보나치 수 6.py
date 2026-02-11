import sys
input = sys.stdin.readline

mod = 1000000007
def fib(n):
    #(f(n), f(n+1)) 반환
    if n == 0:
        return (0, 1)
    
    a, b = fib(n//2)
    c = (a*((2*b - a)%mod))%mod
    d = (a*a + b*b)%mod

    if n%2 == 0:
        return (c, d)
    else:
        return (d, (c+d)%mod)

n = int(input())
print(fib(n)[0])