import sys
input = sys.stdin.readline

isbn = input().rstrip()
rest = 0
check = 0

for i in range(12):
    weight = 1 if i%2 == 0 else 3
    if isbn[i] == '*':
        check = weight
        continue
    
    rest += weight*int(isbn[i])
    rest %= 10

goal = (20-int(isbn[-1]) - rest)%10

if check == 1:
    print(goal)
else:
    dp = {3:1, 6:2, 9:3, 2:4, 5:5, 8:6, 1:7, 4:8, 7:9, 0:0}
    print(dp[goal])