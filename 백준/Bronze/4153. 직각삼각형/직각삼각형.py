import sys
input = sys.stdin.readline

while True:
    nums = sorted(list(map(int, input().split())))
    if nums[0] == 0 and nums[1] == 0 and nums[-1] == 0:
        break
    if nums[0]**2+nums[1]**2 == nums[-1]**2:
        print("right")
    else:
        print("wrong")