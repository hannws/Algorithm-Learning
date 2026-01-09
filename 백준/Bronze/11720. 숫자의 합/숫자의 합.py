import sys

size = int(sys.stdin.readline())
nums = list(sys.stdin.readline().rstrip())
print(sum(list(map(int, nums))))