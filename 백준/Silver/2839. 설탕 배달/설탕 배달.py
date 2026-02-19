import sys
input = sys.stdin.readline

n = int(input())

for five in range(n//5, -1, -1):
    remain = n-5*five
    if remain%3 == 0:
        print(five + remain//3)
        break
else:
    print(-1)