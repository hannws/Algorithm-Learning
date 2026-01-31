import sys
input = sys.stdin.readline

T = int(input())

def backtrack(start):
    if small <= sum(path) <= large:
        return True
    
    for i in range(start, 5):
        path.append(weight[i])

        if backtrack(i+1):
            return True
        
        path.pop()

    return False



for _ in range(T):
    small, large = map(int, input().split())
    weight = list(map(int, input().split()))
    path = []

    if backtrack(0):
        print("YES")
    else:
        print("NO")