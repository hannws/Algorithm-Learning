import sys
S = sys.stdin.readline()
newS = []
judge = ""
for i in S:
    if i != judge:
        newS.append(i)
        judge = i
print(min(newS.count("0"), newS.count("1")))