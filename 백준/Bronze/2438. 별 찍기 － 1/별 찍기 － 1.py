import sys
N = int(sys.stdin.readline())
Ns = []
for i in range(1, N+1):
    Ns.append("*"*i)
sys.stdout.write('\n'.join(Ns))