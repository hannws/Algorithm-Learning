size = int(input())
Alist = list(map(int, input().split()))
Blist = [0]*size
count = 0
for i in range(size):
    for j in range(size):
        if Alist[i] > Alist[j]:
            count += 1
        elif Alist[i] == Alist[j]:
            if i > j:
                count+= 1
    Blist[i] = count
    count = 0
print(*Blist)