def combination(a, b):
    result = 1
    a = min (b-a, a)
    for i in range(1, a+1):
        result = result * (b - a + i) // i
    return result

size = int(input())
for _ in range(size):
    a, b = map(int, input().split())
    print(combination(a, b))