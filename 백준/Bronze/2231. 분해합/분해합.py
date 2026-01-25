import sys
input = sys.stdin.readline

x = int(input())
num = 1

def splitmerge(N):
    total = N
    a = str(N)

    for i in a:
        total += int(i)
    return total

while True:
    if num >= x:
        print(0)
        break
    if splitmerge(num) == x:
        print(num)
        break
    num += 1