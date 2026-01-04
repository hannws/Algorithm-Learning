N, m, M, T, R = map(int, input().split())
ex_time = time = 0
current_Pulse = m

if m + T > M:
    ex_time = N

while ex_time != N:
    if current_Pulse + T <= M:
        current_Pulse += T
        ex_time += 1
    else:
        if current_Pulse - R < m:
            current_Pulse = m
        else:
            current_Pulse -= R
    time += 1

if time:
    print(time)
else:
    print(-1)