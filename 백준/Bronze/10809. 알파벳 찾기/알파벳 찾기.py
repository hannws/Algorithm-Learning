import sys
N = sys.stdin.readline()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
result = []
for i in alpha:
    result.append(N.find(i))
print(*result)