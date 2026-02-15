import sys
input = sys.stdin.readline

T = int(input())
nums = [input().rstrip() for _ in range(T)]

def test1(idx):
    #시작 인덱스를 받고 끝나는 인덱스+1 반환
    # 100+1+ 일 경우 처리

    if num[idx:idx+3] == '100':
        nxt = num[idx+3:].find('1')
        nxt += idx+4

        if nxt == idx+3:
            return -1
        
        temp = num[nxt:]
        if temp.find('0') == -1:
            return len(num)
        elif temp.find('100') != -1 and temp.find('100') < temp.find('0'):
            return nxt+temp.find('100')
        else:
            return nxt + temp.find('0')
    return -1


def test2(idx):
    # (01)+일 경우 처리

    if num[idx:idx+2] == '01':
        curr = idx+2
        while curr < len(num):
            if num[curr: curr+2] != '01':
                break

            if curr + 2 <= len(num):
                curr += 2
            else:
                return -1
        return curr
    return -1

for num in nums:
    start = 0
    while start != -1:
        if start == len(num):
            break

        if num[start] == '1':
            start = test1(start)
        else:
            start = test2(start)

    if start == len(num):
        print("YES")
    else:
        print("NO")