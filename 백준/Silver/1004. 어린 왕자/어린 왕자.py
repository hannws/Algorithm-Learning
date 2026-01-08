import sys
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    cnt = 0

    n = int(sys.stdin.readline())
    for i in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        dis1 = (x1 - cx)**2 + (y1 - cy)**2
        dis2 = (x2 - cx)**2 + (y2 - cy)**2
        if (dis1 > r**2 and dis2 < r**2) or (dis1 < r**2 and dis2 >r**2):
            cnt += 1
    print(cnt)