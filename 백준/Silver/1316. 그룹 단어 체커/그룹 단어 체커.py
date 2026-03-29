import sys
input = sys.stdin.readline

n = int(input())
result = n

for _ in range(n):
    visited = [False]*26
    s = input().rstrip()
    prev = ''

    for i in s:
        ch = ord(i) - ord('a')

        if prev != i:
            if visited[ch]:
                result -= 1
                break
            prev = i
            visited[ch] = True

print(result)