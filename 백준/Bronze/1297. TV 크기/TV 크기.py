import sys

D, H, W = map(int, sys.stdin.readline().split())
rate = ((D**2)/(H**2+W**2))**0.5

print(int(rate*H), int(rate*W))