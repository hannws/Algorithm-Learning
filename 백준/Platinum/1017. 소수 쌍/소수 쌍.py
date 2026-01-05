import sys

is_prime = [True]*2001
is_prime[0] = is_prime[1] = False
for i in range(2, int(2000**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, 2001, i):
            is_prime[j] = False

length = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

even, odd = [], []
for i in numbers:
    if i %2 == 0:
        even.append(i)
    else:
        odd.append(i)

if numbers[0]%2:
    left = odd
    right = even
else:
    left = even
    right = odd
    

left_len = len(left)
right_len = len(right)

if left_len != right_len:
    print(-1)
    sys.exit()

graph = [[] for _ in range(left_len)]
for i in range(left_len):
    for j in range(right_len):
        if is_prime[left[i] + right[j]]:
            graph[i].append(j)

def dfs(u, candid):
    for i in graph[u]:
        if visited[i] or i == candid:
            continue
        visited[i] = True
        if match[i] == -1 or dfs(match[i], candid):
            match[i] = u
            return True
    return False

result = []
for cand in graph[0]:
    match = [-1]*left_len
    match[cand] = 0

    success = True
    for u in range(left_len):
        if u == 0:
            continue
        visited = [False]*right_len
        if not dfs(u, cand):
            success = False
            break
    if success:
        result.append(right[cand])        


if result:
    print(*(sorted(result)))
else:
    print(-1)