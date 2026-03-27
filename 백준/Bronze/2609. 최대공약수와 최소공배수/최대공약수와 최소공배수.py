import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
gcdd = math.gcd(n, m)
lcm = (n*m)//gcdd

print(gcdd, lcm, sep='\n')