import sys
input = sys.stdin.readline

n = int(input())
line = [tuple(map(int, input().split())) for _ in range(n)]
line.sort()

prev1 = 0
prev2 = 0
total = 0

for x1, x2 in line:
    if x1 <= prev2:
        if x2 <= prev2:
            continue
        else:
            total += x2-prev2
            prev2 = x2

    else:
        prev1 = x1
        prev2 = x2
        total += prev2 - prev1

print(total)