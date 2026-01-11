import sys
input = sys.stdin.readline

test = int(input())

fibonums = [(1,0), (0,1)]

for _ in range(test):
    N = int(input())

    length = len(fibonums)
    if length <= N:
        for i in range(length, N+1):
            fibonums.append((fibonums[i-1][0] + fibonums[i-2][0],
                             fibonums[i-1][1] + fibonums[i-2][1]))
            
    print(*fibonums[N])