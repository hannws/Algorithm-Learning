import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().rstrip()
    if s.count('(') != s.count(')'):
        print("NO")
    else:
        a = 0
        for i in s:
            if i == '(':
                a += 1
            else:
                a -= 1
                if a<0:
                    break
        if a == 0:
            print("YES")
        else:
            print("NO")