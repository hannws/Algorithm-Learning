import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nosee = set(input().rstrip() for _ in range(n))
nohear = set(input().rstrip() for _ in range(m))

noseehear = sorted(nosee&nohear)

print(len(noseehear))
sys.stdout.write('\n'.join(noseehear))