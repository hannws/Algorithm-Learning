import sys

result = (0,0)
for i in range(9):
    num = int(sys.stdin.readline())
    if result[0] < num:
        result = (num, i+1)
print(result[0])
print(result[1])