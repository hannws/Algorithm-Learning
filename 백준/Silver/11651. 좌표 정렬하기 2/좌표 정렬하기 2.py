import sys
input = sys.stdin.readline

test = int(input())

points = [tuple(map(int, input().split())) for _ in range(test)]

sys.stdout.write('\n'.join(f"{x[0]} {x[1]}" 
                           for x in sorted(points, key = lambda x: (x[1], x[0]))))