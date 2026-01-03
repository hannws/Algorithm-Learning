size = int(input())
for _ in range(size):
    cost = int(input())
    Quarter = cost // 25
    Dime = (cost%25) // 10
    Nickel = ((cost%25)%10)//5
    Penny = (cost%5)
    print(Quarter, Dime, Nickel, Penny)