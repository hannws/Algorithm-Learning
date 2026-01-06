import sys

nums = [int(sys.stdin.readline()) for _ in range(3)]
result = str(nums[0]*nums[1]*nums[2])
for i in range(10):
    print(result.count(str(i)))