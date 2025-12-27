size = int(input())
s = []
for _ in range(size):
    s.append(input())
result = s[0]
for i in range(1, size):
    for j in range(len(s[i])):
        if result[j] != s[i][j]:
            result = result[:j] + "?" + result[j+1:]
print(result)