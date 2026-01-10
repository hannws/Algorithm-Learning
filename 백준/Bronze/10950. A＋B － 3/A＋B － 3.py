import sys
input = sys.stdin.readline

size = int(input())
for _ in range(size):
    a, b = map(int, input().split())
    print(a+b)