import sys

a,b,c,d,e = map(lambda x: pow(int(x),2,10), sys.stdin.readline().split())
print((a+b+c+d+e)%10)