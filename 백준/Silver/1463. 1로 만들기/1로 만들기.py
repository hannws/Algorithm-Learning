import sys
input = sys.stdin.readline

n = int(input())
cnt = {1:0, 2:1, 3:1}

for i in range(4, n+1):
    temp1 = 1000
    temp2 = 1000
    if i%2 == 0:
        temp1 = cnt[i//2]+1
    if i%3 == 0:
        temp2 = cnt[i//3]+1
    temp3 = cnt[i-1]+1
    cnt[i] = min(temp1, temp2, temp3)
print(cnt[n])