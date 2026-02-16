import sys
input = sys.stdin.readline

def phi(n):
    result = 1
    p = 2

    while p*p <= n:
        if n%p == 0:
            temp = 1
            while n%p == 0:
                n //= p
                temp *= p

            result *= (temp - temp//p)
        p+=1
    
    if n > 1:
        result *= (n-1)
    
    return result


while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(0)
    else:
        print(phi(n))