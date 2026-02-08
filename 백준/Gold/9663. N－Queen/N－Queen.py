import sys
input = sys.stdin.readline

N = int(input())

visited = [False]*N
diag1 = set()
diag2 = set()

def backtrack(col):
    global total

    if col == N:
        total += 1
        return

    for i in range(N):
        if visited[i]:
            continue
        case1 = col+i
        case2 = col-i
        if (case1 in diag1 or case2 in diag2):
            continue

        visited[i] = True
        diag1.add(case1)
        diag2.add(case2)

        backtrack(col+1)

        visited[i] = False
        diag1.remove(case1)
        diag2.remove(case2)



total = 0
backtrack(0)
print(total)