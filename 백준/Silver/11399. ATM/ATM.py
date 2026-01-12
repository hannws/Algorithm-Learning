import sys
input = sys.stdin.readline

n = int(input())
times = sorted(list(map(int, input().split())))
result = 0
for i in range(n):
    result += (n-i)*times[i]
print(result)