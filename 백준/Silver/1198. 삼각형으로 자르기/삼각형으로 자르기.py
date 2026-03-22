import sys
input = sys.stdin.readline

def sizecal(i, j, k):
    A = point[i][0]*point[j][1] + point[j][0]*point[k][1] + point[k][0]*point[i][1]
    B = -(point[i][1]*point[j][0] + point[j][1]*point[k][0] + point[k][1]*point[i][0])
    
    return round(abs(A+B)/2, 9)

n = int(input())
maxsize = -1
point = list(tuple(map(int, input().split())) for _ in range(n))

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            maxsize = max(maxsize, sizecal(i, j, k))

print(maxsize)