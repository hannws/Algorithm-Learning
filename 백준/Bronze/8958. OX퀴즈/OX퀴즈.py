import sys
size = int(sys.stdin.readline())

def cal(olist):
    result = 0
    for i in range(1, len(olist)+1):
        result += i
    return result

for _ in range(size):
    test_case = list(sys.stdin.readline())
    olist = []
    score = 0
    for i in test_case:
        if i == 'O':
            olist.append('O')
        elif i == 'X' and olist:
            score += cal(olist)
            olist = []
    if olist:
        score += cal(olist)
    print(score)