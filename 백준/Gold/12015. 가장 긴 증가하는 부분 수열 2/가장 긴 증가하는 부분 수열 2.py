import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
result = []

for i in range(N):
    if not result or result[-1]<A[i]:
        result.append(A[i])
    else:
        start = 0
        end = len(result) -1
        
        while start < end:
            mid = (start+end)//2

            if A[i] > result[mid]:
                start = mid+1
            else:
                end = mid
        
        result[start] = A[i]

print(len(result))