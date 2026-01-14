import sys
input = sys.stdin.readline

t = int(input())
nums = [int(input()) for _ in range(t)]
max_num = max(nums)

is_prime = [True]*200001
is_prime[0] = is_prime[1] = False

for i in range(2, int(200000**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, 200001, i):
            is_prime[j] = False

def solve(num):
    if not is_prime[num+1]:
        return False
    
    s = str(num)
    for i in range(1, len(s)):
        if not is_prime[int(s[:i])*int(s[i:])+1]:
            return False
    return True

special = [0]*(max_num+1)
special[1] = 1
special[2] = 2
special[3] = 2

for i in range(4, max_num+1):
    if solve(i):
        special[i] = special[i-1]+1
    else:
        special[i] = special[i-1]

for n in nums:
    print(special[n])