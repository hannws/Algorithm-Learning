import sys
input = sys.stdin.readline

n = int(input())
r = n//5

while r+1:
    if (n-5*r)%3 == 0:
        print(r + (n-5*r)//3)
        sys.exit()
    r -= 1

print(-1)