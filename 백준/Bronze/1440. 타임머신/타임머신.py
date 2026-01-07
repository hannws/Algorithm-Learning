import sys

a,b,c = (map(int, sys.stdin.readline().split(":")))
test = [(a,b,c), (a,c,b), (b,a,c), (b,c,a), (c,a,b), (c,b,a)]
cnt = 0
for case in test:
    if case[0] <= 12 and case[0] >= 1 and case[1] <= 59 and case[1] >=0 and case[2] <= 59 and case[2] >=0:
        cnt +=1
print(cnt)