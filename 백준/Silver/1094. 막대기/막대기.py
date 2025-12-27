size = 64
x = int(input())
number = 0
while (x):
    if size <= x:
        x = x - size
        number += 1
    size = size//2

print(number)