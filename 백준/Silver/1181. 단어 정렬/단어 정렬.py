size = int(input())
words = []
for i in range(size):
    word = input()
    words.append(word)
print(*sorted(set(words), key = lambda x : (len(x), x)), sep='\n')