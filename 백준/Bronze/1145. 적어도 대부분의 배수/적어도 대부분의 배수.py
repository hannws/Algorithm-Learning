numbers = list(map(int, input().split()))
result = min(numbers)
while True:
    cnt = 0
    for i in numbers:
        if result % i == 0:
            cnt += 1
    if cnt >=3:
        print(result)
        break
    result += 1