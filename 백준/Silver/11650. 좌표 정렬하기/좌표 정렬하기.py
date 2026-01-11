import sys
input = sys.stdin.readline

test = int(input())

nums = []
for _ in range(test):
    num = tuple(map(int, input().split()))
    nums.append(num)

sys.stdout.write('\n'.join(map(lambda x: f"{x[0]} {x[1]}",sorted(nums))))