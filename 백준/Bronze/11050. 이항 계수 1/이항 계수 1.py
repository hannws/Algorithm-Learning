import sys
N, K = map(int, sys.stdin.readline().split())
result = 1
for i in range(1, K+1):
    result = (result*(N-K+i))//i
sys.stdout.write(str(result))