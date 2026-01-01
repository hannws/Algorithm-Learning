n1= input()
n2 = input()
n3 = input()
match n1:
    case "black":
        result = 0
    case "brown":
        result = 10
    case "red":
        result = 20
    case "orange":
        result = 30
    case "yellow":
        result = 40
    case "green":
        result = 50
    case "blue":
        result = 60
    case "violet":
        result = 70
    case "grey":
        result = 80
    case "white":
        result = 90
match n2:
    case "black":
        result += 0
    case "brown":
        result += 1
    case "red":
        result += 2
    case "orange":
        result += 3
    case "yellow":
        result += 4
    case "green":
        result += 5
    case "blue":
        result += 6
    case "violet":
        result += 7
    case "grey":
        result += 8
    case "white":
        result += 9
match n3:
    case "black":
        result *= 1
    case "brown":
        result *= 10
    case "red":
        result *= 100
    case "orange":
        result *= 1000
    case "yellow":
        result *= 10000
    case "green":
        result *= 100000
    case "blue":
        result *= 1000000
    case "violet":
        result *= 10000000
    case "grey":
        result *= 100000000
    case "white":
        result *= 1000000000
print(result)