import sys
input = sys.stdin.readline

N = int(input())
dice = list(map(int, input().split()))

if N == 1:
    print(sum(dice) - max(dice))
    sys.exit()

min1 = min(dice)

min2 = float('inf')
for i in range(6):
    for j in range(i+1, 6):
        if i + j == 5:
            continue
        min2 = min(min2, dice[i] + dice[j])

min3 = float('inf')
for i in range(6):
    for j in range(i+1, 6):
        if i + j == 5:
            continue
        for k in range(j+1, 6):
            if i+k == 5 or j+k == 5:
                continue
            min3 = min(min3, dice[i] + dice[j] + dice[k])


usemin1 = ((N-2)**2)*5 + (N-2)*4
usemin2 = 4*(2*N - 3)
usemin3 = 4
print(min1*usemin1 + min2*usemin2 + min3*usemin3)