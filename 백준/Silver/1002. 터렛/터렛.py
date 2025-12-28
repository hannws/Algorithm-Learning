size = int(input())
for _ in range(size):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    if(x1 == x2 and y1 == y2):
        if(r1 == r2):
            print(-1)
        else:
            print(0)
    else:
        if(dis > r1+r2):
            print(0)
        elif(dis == r1 + r2):
            print(1)
        else:
            if(r2 == dis + r1 or r1 == dis + r2):
                print(1)
            elif (r2 > dis + r1 or r1 > dis + r2):
                print(0)
            else:
                print(2)