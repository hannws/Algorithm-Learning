length = int(input())
info = input()

couple_cnt = info.count("LL")

if couple_cnt == 0:
    print(length)
else:
    print(length - couple_cnt + 1)