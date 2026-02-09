import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

black =[]
white = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            if (i+j)%2 == 0:
                black.append((i,j))
            else:
                white.append((i, j))

def solve(square):
    diag1 = set() #\
    diag2 = set() #/

    def backtrack(idx):
        if idx == len(square):
            return 0
        
        x, y = square[idx]
        result = backtrack(idx+1)

        if (x+y not in diag1) and (x-y not in diag2):
            diag1.add(x+y)
            diag2.add(x-y)
            result = max(result, 1 + backtrack(idx+1))
            diag1.remove(x+y)
            diag2.remove(x-y)
        
        return result
    return backtrack(0)

print(solve(white) + solve(black))