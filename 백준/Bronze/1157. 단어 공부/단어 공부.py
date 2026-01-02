sentence = input().upper()
counts = dict()
for i in sentence:
    counts[i] = counts.get(i, 0) + 1
max_cnt = max(counts.values())

frequents = [char for char, cnt in counts.items() if cnt == max_cnt]

if len(frequents) > 1:
    print("?")
else:
    print(frequents[0])