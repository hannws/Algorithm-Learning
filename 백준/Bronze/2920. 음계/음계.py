import sys
nums = list(map(int, sys.stdin.readline().split()))
ascend = [1,2,3,4,5,6,7,8]
descend = [8,7,6,5,4,3,2,1]
if nums == ascend:
    print("ascending")
elif nums == descend:
    print("descending")
else:
    print("mixed")