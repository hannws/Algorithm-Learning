size = int(input())
for _ in range(size):
    cost = int(input())
    Quarter = cost // 25
    Dime = (cost - 25*Quarter) // 10
    Nickel = (cost - 25*Quarter - 10*Dime)//5
    Penny = (cost - 25*Quarter - 10*Dime - 5*Nickel)//1
    print(Quarter, Dime, Nickel, Penny)