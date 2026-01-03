length = int(input())
info = input()

info_len, new_info, i = len(info), [], 0
while (info_len):
    if(info[i] == "S"):
        new_info.append("S")
        i += 1
        info_len -= 1
    elif(info[i] == "L"):
        new_info.append("LL")
        i+=2
        info_len -= 2

cupholders, i, cnt = [1]*(len(new_info)+1), 0, 0
for case in new_info:
    if(case =="S"):
        if cupholders[i] == 1:
            cupholders[i] = 0
        else:
            cupholders[i+1] = 0
        cnt += 1
    elif case == "LL":
        if cupholders[i] == 1:
            cupholders[i], cupholders[i+1] = 0, 0
            cnt += 2
        else:
            cupholders[i+1] = 0
            cnt += 1
    i += 1

print(cnt)