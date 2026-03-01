import sys
input = sys.stdin.readline

N = int(input())
point = [tuple(map(int, input().split())) for _ in range(N)]
point.append(point[0])

A = 0
B = 0

for i in range(N):
    A += point[i][0]*point[i+1][1]
    B -= point[i][1]*point[i+1][0]

print(round((abs(A+B))/2, 1))