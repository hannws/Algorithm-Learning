import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
total = 0

for i in range(n):
    total += (ord(s[i]) - ord('a') + 1)*(31**i)

print(total)