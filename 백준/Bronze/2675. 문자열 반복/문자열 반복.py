import sys
N = int(sys.stdin.readline())
for _ in range(N):
    R, S = sys.stdin.readline().split()
    R = int(R)
    S = list(S)
    for i in range(len(S)):
        S[i] = S[i]*R
    print("".join(S))