import sys
input = sys.stdin.readline

x = int(input())
start = 1

while True:
    if x-start > 0:
        x -= start
        start += 1
        continue
    if start %2 == 0:
        denominator = start+1 - x
        numerator = x
    else:
        numerator = start+1 - x
        denominator = x
    break
print(f"{numerator}/{denominator}")