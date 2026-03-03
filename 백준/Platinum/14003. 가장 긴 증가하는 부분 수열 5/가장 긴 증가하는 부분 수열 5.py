import sys
import bisect
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
result = []
pos = [0]*N

for i in range(N):
    idx = bisect.bisect_left(result, A[i])

    if len(result)==idx:
        result.append(A[i])
    else:
        result[idx] = A[i]
    
    pos[i] = idx

length = len(result)
print(length)

B = []
cur = length-1

for i in range(N-1, -1, -1):
    if pos[i] == cur:
        B.append(A[i])
        cur -= 1
    elif cur == -1:
        break

B.reverse()
print(*B)