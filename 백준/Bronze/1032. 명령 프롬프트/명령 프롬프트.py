size = int(input())
s = [input() for _ in range(size)]

result = list(s[0])

for i in range(1, size):
    for j in range(len(result)):
        if result[j] != '?' and result[j] != s[i][j]:
            result[j] = '?'

print(''.join(result))