import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

M = 1234567891
total = 0
r = 1

for i in range(n):
    value = ord(s[i]) - ord('a') +1
    total = (total + value*r)%M
    r = (r*31)%M

print(total)