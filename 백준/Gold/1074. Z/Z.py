import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

def dfs(N, r, c):
    if N==1:
        if r==1:
            if c==1:
                return 0
            else:
                return 1
        else:
            if c==1:
                return 2
            else:
                return 3
    total = 0
    comp = 2**(N-1)
    if r > comp:
        r -= comp
        total += 2*(comp**2)
    if c > comp:
        c -= comp
        total += comp**2
    
    return total + dfs(N-1, r, c)

result = dfs(N,r+1,c+1)
print(result)