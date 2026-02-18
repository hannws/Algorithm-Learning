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

divisors = []
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        divisors.append(i)
        if i != n // i:
            divisors.append(n // i)

answer = float('inf')

for d in divisors:
    if d * phi(d) == n:
        answer = min(answer, d)

print(answer if answer != float('inf') else -1)