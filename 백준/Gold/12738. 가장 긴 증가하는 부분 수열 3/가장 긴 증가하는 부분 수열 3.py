import sys
import bisect
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
result = []

for num in A:
    idx = bisect.bisect_left(result, num)

    if idx == len(result):
        result.append(num)
    else:
        result[idx] = num

print(len(result))