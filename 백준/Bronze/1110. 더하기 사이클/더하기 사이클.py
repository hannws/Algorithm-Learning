N = int(input())
result, count = N, 0

while True:
    S1 = (result//10 + result%10)%10
    result = (result%10)*10 + S1
    count += 1
    if(result == N):
        break

print(count)