import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = [input().rstrip() for _ in range(N)]
poke_dict= dict()
poke_revers_dict = dict()
for i, j in enumerate(pokemon):
    poke_dict[i+1] = j
    poke_revers_dict[j] = i+1

for _ in range(M):
    query = input().rstrip()
    if query.isdigit():
        print(poke_dict[int(query)])
    else:
        print(poke_revers_dict[query])