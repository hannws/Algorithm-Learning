import sys
size = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(size)]
numbers.sort()
sys.stdout.write('\n'.join(map(str, numbers)))