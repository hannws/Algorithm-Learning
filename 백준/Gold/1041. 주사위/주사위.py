import sys
input = sys.stdin.readline

N = int(input())
dice = list(map(int, input().split()))

if N == 1:
    print(sum(dice) - max(dice))
    sys.exit()

min1 = min(dice)

a = min(dice[0], dice[5])
b = min(dice[1], dice[4])
c = min(dice[2], dice[3])

min2 = min(a+b, a+c, b+c)
min3 = a+b+c


usemin1 = ((N-2)**2)*5 + (N-2)*4
usemin2 = 4*(2*N - 3)
usemin3 = 4
print(min1*usemin1 + min2*usemin2 + min3*usemin3)