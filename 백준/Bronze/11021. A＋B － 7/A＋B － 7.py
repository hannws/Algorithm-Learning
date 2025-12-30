size = int(input())
for i in range(size):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {a+b}")