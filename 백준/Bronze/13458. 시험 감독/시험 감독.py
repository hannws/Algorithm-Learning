import math
n = int(input())
numbers = list(map(int, input().split()))
B, C = map(int, input().split())
result = n
for i in range(n):
    numbers[i] -= B
    if(numbers[i] >0):
        result += math.ceil(numbers[i]/C)
    else:
        continue
print(result)