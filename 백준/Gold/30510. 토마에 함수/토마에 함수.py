import sys
input = sys.stdin.readline

def phi(n):
    result = n
    p = 2

    while p*p <= n:
        if n%p == 0:
            while n%p == 0:
                n//=p
            result = result - result//p
        p += 1
    
    if n > 1:
        result -= result//n
    return result


p, q = map(int, input().split())
end = q//p
total = 1

for i in range(1, end+1):
    total += phi(i)

print(total)