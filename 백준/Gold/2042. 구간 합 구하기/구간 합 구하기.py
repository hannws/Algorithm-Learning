import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = [0]*(N+1)
tree = [0]*(N+1)
#Fenwick tree

def update(i, diff):
    while i <= N:
        tree[i] += diff
        i += (i&-i)

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i&-i)
    return result

for i in range(1, N+1):
    num = int(input())
    arr[i] = num
    update(i, num)

for _ in range(M+K):
    a, b, c = map(int, input().split())

    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        update(b, diff)
    else:
        print(prefix_sum(c) - prefix_sum(b-1))