import sys
input = sys.stdin.readline

result = ""
while True:
    s = input().rstrip()
    if (int(s) == 0):
        break
    if s == s[::-1]:
        result += 'yes\n'
    else:
        result += 'no\n'

print(result)