import sys
input = sys.stdin.readline

N = int(input())
meeting = [tuple(map(int, input().split())) for _ in range(N)]
meeting.sort(key=lambda x: (x[1], x[0]))

end = 0
cnt = 0

for start2, end2 in meeting:
    if start2 >= end:
        cnt += 1
        end = end2

print(cnt)