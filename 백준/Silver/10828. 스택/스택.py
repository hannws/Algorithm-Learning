import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()

for _ in range(n):
    command = input().split()
    if len(command) == 2:
        value = command[1]
        command = command[0]
    else:
        command = command[0]
    
    match command:
        case "push":
            dq.append(value)
        case "pop":
            if dq:
                print(dq.pop())
            else:
                print(-1)
        case "size":
            print(len(dq))
        case "empty":
            if not dq:
                print(1)
            else:
                print(0)
        case "top":
            if dq:
                print(dq[-1])
            else:
                print(-1)