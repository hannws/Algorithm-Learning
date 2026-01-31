import sys
input = sys.stdin.readline

T = int(input())

def backtrack(start, total):
    if small <= total <= large:
        return True
    elif total > large:
        return False

    for i in range(start, 5):
        if backtrack(i+1, total + weight[i]):
            return True

    return False



for _ in range(T):
    small, large = map(int, input().split())
    weight = list(map(int, input().split()))
    path = []

    if backtrack(0, 0):
        print("YES")
    else:
        print("NO")