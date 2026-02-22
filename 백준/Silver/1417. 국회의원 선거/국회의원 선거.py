import sys
import heapq
input = sys.stdin.readline

N = int(input())
dasom = int(input())

if N ==1:
    print(0)
    sys.exit(0)

heap = []
for _ in range(N-1):
    vote = int(input())
    heapq.heappush(heap, -vote)

buy = 0

while heap and dasom <= -heap[0]:
    top = -heapq.heappop(heap)
    top -= 1
    dasom += 1
    buy += 1
    heapq.heappush(heap, -top)

print(buy)