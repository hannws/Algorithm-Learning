import sys
input = sys.stdin.readline

test = int(input())
difficulty = [int(input()) for _ in range(test)]
difficulty.sort()
leng = len(difficulty)

n = int((leng*15)/100 + 0.5)
difficulty = difficulty[n : leng - n]

new_len = len(difficulty)
if new_len:
    print(int(sum(difficulty)/new_len+0.5))
else:
    print(0)