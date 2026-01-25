import sys
input = sys.stdin.readline

x = int(input())
length = len(str(x))
num = max(1, x - 9*length)

def splitmerge(N):
    return N+sum(map(int, str(N)))

answer = 0
for i in range(num, x):
    if splitmerge(i) == x:
        answer = i
        break
print(answer)