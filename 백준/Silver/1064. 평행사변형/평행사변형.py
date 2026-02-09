import sys
import math
input = sys.stdin.readline

x1, y1, x2, y2, x3, y3 = map(int, input().split())

A = (x1, y1)
B = (x2, y2)
C = (x3, y3)

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

if (x2-x1)*(y3-y1) == (y2-y1)*(x3-x1):
    print(-1)
    sys.exit()

diff = []
diff.append(2*(dist(A, B) + dist(A,C)))
diff.append(2*(dist(B, A) + dist(B, C)))
diff.append(2*(dist(C, A) + dist(C, B)))

print(max(diff) - min(diff))