n = [list(input()) for _ in range(8)]
result = 0
for i in range(8):
    for j in range(8):
        if (i + j)%2 == 0:
            result += (n[i][j] == "F")
print(result)