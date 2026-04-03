import sys
input = sys.stdin.readline

l = int(input())
nums = sorted(map(int, input().split()))
n = int(input())

small = 0
big = 0
for i in range(len(nums)):
    if nums[i] == n:
        print(0)
        sys.exit(0)
    if nums[i] > n:
        if i == 0:
            big = nums[i]
        else:
            big = nums[i]
            small = nums[i-1]
        break

diff1 = big - n - 1
diff2 = n-small-1

if diff1 == 0 and diff2 == 0:
    print(0)
elif diff1 == 0:
    print(diff2)
elif diff2 == 0:
    print(diff1)
else:
    print(diff2 + diff1*(diff2+1))