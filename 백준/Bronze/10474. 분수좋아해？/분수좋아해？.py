x, y = map(int, input().split())
while(x!=0 and y != 0):
    print(f"{x//y} {x%y} / {y}")
    x, y = map(int, input().split())