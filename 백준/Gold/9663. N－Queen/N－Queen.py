import sys
input = sys.stdin.readline

N = int(input())

def backtrack(row, cols, d1, d2):
    if row == N:
        return 1
    
    cnt = 0
    available = ((1<<N)-1) & ~(cols|d1|d2)

    while available:
        p = available & -available
        available -= p
        cnt += backtrack(row + 1, cols | p, (d1|p) <<1, (d2|p) >> 1)
    return cnt

print(backtrack(0, 0, 0, 0))