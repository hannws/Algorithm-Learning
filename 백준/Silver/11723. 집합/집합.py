import sys
input = sys.stdin.readline

m = int(input())

s = set()
for _ in range(m):
    data = input().split()
    if len(data) == 1:
        oper = data[0]
    else:
        oper = data[0]
        x = int(data[1])

    match oper:
        case "add":
            s.add(x)
        case "remove":
            if x in s:
                s.remove(x)
        case "check":
            if x in s:
                print(1)
            else:
                print(0)
        case "toggle":
            if x in s:
                s.remove(x)
            else:
                s.add(x)
        case "all":
            s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        case "empty":
            s.clear()