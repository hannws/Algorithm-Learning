import sys

row, col = map(int, sys.stdin.readline().split())

wbset = ['W' if i%2==0 else 'B' for i in range(col)]
bwset = ['W' if i%2==1 else 'B' for i in range(col)]

for_cal = [[] for _ in range(row)]


for i in range(row):
    roww = list(sys.stdin.readline().rstrip('\n'))
    if i%2==0: test = wbset
    else: test = bwset
    temp = []
    for j in range(col):
        if roww[j] == test[j]:
            temp.append(0)
        else:
            temp.append(1)
    for k in range(col - 7):
        for_cal[i].append(sum(temp[k:8+k]))

result = 64
for j in range(col - 7):
    for i in range(row - 7):
        temp_result = 0
        for k in range(i, i+8):
            temp_result += for_cal[k][j]
        temp_result = min(temp_result, 64-temp_result)
        if temp_result < result:
            result = temp_result

print(result)