size = int(input())
roster = {}
for _ in range(size):
    name = input()[0]
    roster[name] = roster.get(name, 0) + 1
max_roster = max(roster.values())
if(max_roster >= 5):
    final_roster = sorted([char for char, cnt in roster.items() if cnt >= 5])
    print("".join(final_roster))
else:
    print("PREDAJA")