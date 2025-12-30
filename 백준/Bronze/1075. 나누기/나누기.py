N = int(input())
F = int(input())
BN= N//100
result = (F - ((BN%F)*100)%F)
if(result == F):
    print("00")
else:
    print(f"{result:02d}")