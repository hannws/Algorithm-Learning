import re
import sys
input = sys.stdin.readline

N = int(input())
s = input().strip()
idx = s.find('*')
tofind = s[:idx] + '.*' + s[idx+1:]
pattern = re.compile(tofind)

for _ in range(N):
    s = input().strip()
    if pattern.fullmatch(s):
        print("DA")
    else:
        print("NE")