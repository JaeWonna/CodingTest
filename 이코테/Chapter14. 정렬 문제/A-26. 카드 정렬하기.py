import heapq

n = int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

total = 0
while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    sum_value = a + b
    heapq.heappush(heap, sum_value)
    total += sum_value

print(total)
