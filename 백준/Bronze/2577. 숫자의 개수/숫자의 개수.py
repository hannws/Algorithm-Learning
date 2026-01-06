import sys

nums = [int(sys.stdin.readline()) for _ in range(3)]
test = [0,1,2,3,4,5,6,7,8,9]
cnt =[0,0,0,0,0,0,0,0,0,0]
result = str(nums[0]*nums[1]*nums[2])
for i in test:
    cnt[i] = result.count(f"{i}")
print('\n'.join(map(str, cnt)))