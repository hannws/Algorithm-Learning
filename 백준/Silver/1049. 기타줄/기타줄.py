import sys
input = sys.stdin.readline

N, M = map(int, input().split())
price = [tuple(map(int, input().split())) for _ in range(M)]
pack = min(p[0] for p in price)
each = min(p[1] for p in price)

answer = min((N//6)*pack + (N%6)*each, ((N//6)+1)*pack, each*N)
print(answer)