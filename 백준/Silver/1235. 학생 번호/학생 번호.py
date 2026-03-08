import sys
input = sys.stdin.readline

N = int(input())

id = []
for _ in range(N):
    id.append(input().rstrip())

length = len(id[0])
result = length
for i in range(length):
    test = set()
    for j in range(N):
        test.add(id[j][(length-1-i):])
    
    if len(test) == N:
        result = i+1
        break

print(result)