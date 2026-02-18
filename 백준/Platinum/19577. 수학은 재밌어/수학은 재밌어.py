import sys
input = sys.stdin.readline

n = int(input())

def get_prime_factors(n):
    result = []
    p = 2

    while p*p <= n:
        if n%p == 0:
            while n%p == 0:
                n //= p
            result.append(p)
        p+=1
    
    if n > 1:
        result.append(n)
    return result

test = sorted(get_prime_factors(n), reverse=True)
curr = n
result = 1

for i in test:
    if curr == 1:
        break
    if curr%(i*(i-1)) == 0:
        k=1
        curr //= i*(i-1)

        div = i*i
        while curr%div == 0:
            curr //= div
            k+=1
        
        result *= i**k

if curr == 1:
    print(result)
else:
    print(-1)