import sys
input = sys.stdin.readline

size = int(input())
nums = set(input().split())

size2 = int(input())
num = (input().split())

result = ["1" if i in nums else "0" for i in num]
sys.stdout.write('\n'.join(result))