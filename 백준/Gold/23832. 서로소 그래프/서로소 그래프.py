import sys
input = sys.stdin.readline

n = int(input())

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

result = 0
for i in range(2, n+1):
    result += phi(i)
    
print(result)