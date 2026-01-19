import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
comp = sorted(set(X))
rank = {value:idx for idx, value in enumerate(comp)}

result = [rank[x] for x in X]

print(*result)