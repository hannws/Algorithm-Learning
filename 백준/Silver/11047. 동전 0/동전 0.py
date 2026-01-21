import sys
input = sys.stdin.readline

N, K = map(int, input().split())
money = [int(input()) for _ in range(N)]
money.sort(reverse=True)

cnt = 0
current = K
for i in money:
    howmany = current//i
    if howmany:
        current -= howmany*i
        cnt += howmany

print(cnt)