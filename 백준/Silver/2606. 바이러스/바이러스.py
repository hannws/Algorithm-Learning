import sys
input = sys.stdin.readline

num_of_computer = int(input())
n = int(input())

info = [[] for _ in range(num_of_computer)]

def connect(n):
    for i in info[n]:
        if visited[i]: continue
        visited[i] = True
        if info[i]:
            connect(i)
    

for _ in range(n):
    x, y = map(lambda x: int(x)-1, input().split())
    info[x].append(y)
    info[y].append(x)

visited = [False]*num_of_computer
visited[0] = True
connect(0)

print(sum(visited)-1)