import sys
input = sys.stdin.readline

N, K = map(int, input().split())
memo = dict()
for _ in range(N):
    site, pw = input().split()
    memo[site] = pw

for _ in range(K):
    req = input().rstrip()
    print(memo[req])