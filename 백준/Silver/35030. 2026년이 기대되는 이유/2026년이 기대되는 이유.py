import sys
input = sys.stdin.readline

t = int(input())

special = [0]*100001
special[1] = 1
special[2] = 2
special[3] = 2

end = 3

def special_func(end, n):
    while end < n:
        if solve(end+1):
            special[end+1] = special[end] + 1
        else:
            special[end+1] = special[end]
        end += 1
    return end

def solve(num):
    if not is_prime(num+1):
        return False
    num = str(num)
    length = len(num)
    if length >= 2:
        for i in range(1, length):
            test = int(num[:i])*int(num[i:])+1
            if not is_prime(test):
                return False
    return True

def is_prime(n):
    if n == 0 or n == 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

for _ in range(t):
    N = int(input())
    end = special_func(end, N)
    print(special[N])