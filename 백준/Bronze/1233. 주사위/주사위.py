s1, s2, s3 = map(int, input().split())
result = list()
for _ in range(s1 + s2 + s3):
    result.append(0)
for i in range(s1):
    for j in range(s2):
        for k in range(s3):
            result[i+j+k] += 1
n = max(result)
print(result.index(n) + 3)