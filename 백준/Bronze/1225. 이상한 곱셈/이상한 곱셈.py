import sys

A, B = map(lambda x: list(map(int, x)),sys.stdin.readline().split())

result = sum(A)*sum(B)

print(result)